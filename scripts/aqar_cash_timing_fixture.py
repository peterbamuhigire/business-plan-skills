"""Calculate a synthetic collection-lag sensitivity for the P13 test fixture.

This is an operational cash-timing demonstration, not an Aqar forecast,
accounting model, market estimate, or funding recommendation.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


FIXTURE = (
    Path(__file__).resolve().parents[1]
    / "tests"
    / "fixtures"
    / "aqar-expansion-cash-timing.json"
)
REQUIRED_ASSUMPTION_FIELDS = {
    "id",
    "name",
    "value",
    "unit",
    "source_id",
    "effective_date",
    "owner",
    "classification",
}


def validate_fixture(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["fixture must be an object"]
    if not str(data.get("fixture_label", "")).startswith("FICTIONAL TEST DATA"):
        errors.append("fixture must be labelled fictional test data")
    scope = data.get("scope")
    if not isinstance(scope, dict) or any(
        scope.get(key) != "NOT_ASSESSED"
        for key in ("customer", "geography", "product", "market_denominator")
    ):
        errors.append("missing Aqar scope must remain NOT_ASSESSED")
    finance = data.get("finance_boundary")
    if not isinstance(finance, dict) or finance.get("revenue_recognition") != "NOT_ASSESSED":
        errors.append("revenue recognition must remain NOT_ASSESSED")
    model = data.get("model")
    if not isinstance(model, dict):
        return errors + ["model must be an object"]
    for key in (
        "periods",
        "opening_cash_scu",
        "monthly_billings_scu",
        "monthly_cash_costs_scu",
        "available_liquidity_scu",
        "collection_rate_percent",
    ):
        if not isinstance(model.get(key), int) or isinstance(model.get(key), bool):
            errors.append(f"model.{key} must be an integer")
    if errors:
        return errors
    if model["periods"] <= 0 or model["collection_rate_percent"] != 100:
        errors.append("fixture requires positive periods and a fixed 100% collection rate")
    if any(
        model[key] < 0
        for key in (
            "opening_cash_scu",
            "monthly_billings_scu",
            "monthly_cash_costs_scu",
            "available_liquidity_scu",
        )
    ):
        errors.append("cash, billings, costs, and liquidity must be non-negative")
    assumptions = data.get("assumptions")
    if not isinstance(assumptions, list) or not assumptions:
        errors.append("assumptions must be a non-empty list")
    else:
        for assumption in assumptions:
            if not isinstance(assumption, dict):
                errors.append("assumption records must be objects")
                continue
            missing = REQUIRED_ASSUMPTION_FIELDS - assumption.keys()
            if missing:
                errors.append(f"assumption missing fields: {', '.join(sorted(missing))}")
            if assumption.get("source_id") not in {
                item.get("id") for item in data.get("synthetic_sources", [])
                if isinstance(item, dict)
            }:
                errors.append(f"assumption {assumption.get('id', '?')} has no source record")
    scenarios = data.get("scenarios")
    if not isinstance(scenarios, list) or len(scenarios) != 3:
        errors.append("exactly three scenarios are required")
    else:
        ids = [item.get("id") for item in scenarios if isinstance(item, dict)]
        if set(ids) != {"upside", "base", "downside"} or len(ids) != len(scenarios):
            errors.append("scenario ids must be upside, base, and downside")
        known_sources = {
            item.get("id")
            for item in data.get("synthetic_sources", [])
            if isinstance(item, dict)
        }
        for scenario in scenarios:
            if not isinstance(scenario, dict):
                errors.append("scenario records must be objects")
                continue
            if not isinstance(scenario.get("collection_lag_months"), int) or isinstance(
                scenario.get("collection_lag_months"), bool
            ):
                errors.append(f"scenario {scenario.get('id', '?')} needs an integer collection lag")
            elif scenario["collection_lag_months"] < 0:
                errors.append(f"scenario {scenario.get('id', '?')} collection lag must be non-negative")
            if (
                not isinstance(scenario.get("source_id"), str)
                or scenario["source_id"] not in known_sources
                or not scenario.get("effective_date")
                or not scenario.get("owner")
            ):
                errors.append(f"scenario {scenario.get('id', '?')} needs source, date, and owner")
            if not scenario.get("management_action"):
                errors.append(f"scenario {scenario.get('id', '?')} needs a management action")
    return errors


def simulate(data: dict[str, Any], scenario: dict[str, Any]) -> dict[str, Any]:
    """Return a monthly invoice/cash bridge with fixed billings and costs."""
    model = data["model"]
    periods = model["periods"]
    lag = scenario["collection_lag_months"]
    billings = [model["monthly_billings_scu"]] * periods
    receipts = [0] * periods
    for invoice_month, amount in enumerate(billings):
        receipt_month = invoice_month + lag
        if receipt_month < periods:
            receipts[receipt_month] += amount
    costs = [model["monthly_cash_costs_scu"]] * periods
    cash = model["opening_cash_scu"]
    balances: list[int] = []
    for receipt, cost in zip(receipts, costs, strict=True):
        cash += receipt - cost
        balances.append(cash)
    trough = min([model["opening_cash_scu"], *balances])
    funding_need = max(0, -trough)
    liquidity = model["available_liquidity_scu"]
    funding_gap = max(0, funding_need - liquidity)
    if funding_gap:
        action = "DEFER_ROLLOUT_UNTIL_FUNDING_OWNER_APPROVES"
    elif funding_need:
        action = "USE_BUFFER_AND_HOLD_NEXT_MILESTONE_UNTIL_COLLECTIONS_CONFIRM"
    else:
        action = "PROCEED_SYNTHETIC_BASELINE"
    return {
        "scenario": scenario["id"],
        "monthly_billings_scu": billings,
        "monthly_receipts_scu": receipts,
        "monthly_costs_scu": costs,
        "ending_cash_scu": balances,
        "cash_trough_scu": trough,
        "required_funding_scu": funding_need,
        "available_liquidity_scu": liquidity,
        "unfunded_gap_scu": funding_gap,
        "ending_receivables_scu": sum(billings) - sum(receipts),
        "management_action": action,
    }


def load_fixture(path: Path = FIXTURE) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    errors = validate_fixture(data)
    if errors:
        raise ValueError("; ".join(errors))
    return data


def run_fixture(path: Path = FIXTURE) -> list[dict[str, Any]]:
    data = load_fixture(path)
    results = [simulate(data, scenario) for scenario in data["scenarios"]]
    if len({tuple(row["monthly_billings_scu"]) for row in results}) != 1:
        raise ValueError("billings changed across collection-only scenarios")
    return results


if __name__ == "__main__":
    print(json.dumps(run_fixture(), indent=2))
