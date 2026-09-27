"""Calculate a synthetic collection-lag sensitivity for the P13 test fixture.

This is an operational cash-timing demonstration, not an Aqar forecast,
accounting model, market estimate, or funding recommendation.
"""

from __future__ import annotations

import json
from datetime import date
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
    "model_key",
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
    sources = data.get("synthetic_sources")
    if not isinstance(sources, list) or not sources:
        errors.append("synthetic_sources must be a non-empty list")
        known_sources: set[str] = set()
    else:
        source_ids: list[str] = []
        for source in sources:
            if not isinstance(source, dict):
                errors.append("synthetic source records must be objects")
                continue
            source_id = source.get("id")
            description = source.get("description")
            if not isinstance(source_id, str) or not source_id.strip():
                errors.append("synthetic source id must be a non-empty string")
            else:
                source_ids.append(source_id)
            if not isinstance(description, str) or not description.strip():
                errors.append(f"synthetic source {source_id or '?'} needs a description")
        if len(source_ids) != len(set(source_ids)):
            errors.append("synthetic source ids must be unique")
        known_sources = set(source_ids)

    def valid_date(value: Any) -> bool:
        if not isinstance(value, str) or not value.strip():
            return False
        try:
            date.fromisoformat(value)
        except ValueError:
            return False
        return True

    assumptions = data.get("assumptions")
    if not isinstance(assumptions, list) or not assumptions:
        errors.append("assumptions must be a non-empty list")
    else:
        assumption_ids: list[str] = []
        model_assumptions: dict[str, int] = {}
        expected_units = {
            "monthly_billings_scu": "SCU/month",
            "monthly_cash_costs_scu": "SCU/month",
            "available_liquidity_scu": "SCU",
        }
        for assumption in assumptions:
            if not isinstance(assumption, dict):
                errors.append("assumption records must be objects")
                continue
            missing = REQUIRED_ASSUMPTION_FIELDS - assumption.keys()
            if missing:
                errors.append(f"assumption missing fields: {', '.join(sorted(missing))}")
                continue
            assumption_id = assumption.get("id")
            if not isinstance(assumption_id, str) or not assumption_id.strip():
                errors.append("assumption id must be a non-empty string")
            else:
                assumption_ids.append(assumption_id)
            for field in ("name", "unit", "owner", "classification"):
                if not isinstance(assumption[field], str) or not assumption[field].strip():
                    errors.append(f"assumption {assumption_id or '?'} needs non-empty {field}")
            source_id = assumption.get("source_id")
            if not isinstance(source_id, str) or source_id not in known_sources:
                errors.append(f"assumption {assumption.get('id', '?')} has no source record")
            if not valid_date(assumption.get("effective_date")):
                errors.append(f"assumption {assumption_id or '?'} needs an ISO calendar effective_date")
            if assumption.get("classification") != "synthetic test assumption":
                errors.append(f"assumption {assumption_id or '?'} must remain a synthetic test assumption")
            model_key = assumption.get("model_key")
            if not isinstance(model_key, str) or model_key not in expected_units:
                errors.append(f"assumption {assumption_id or '?'} has an unsupported model_key")
                continue
            if assumption.get("unit") != expected_units[model_key]:
                errors.append(f"assumption {assumption_id or '?'} unit does not match {model_key}")
            value = assumption.get("value")
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                errors.append(f"assumption {assumption_id or '?'} value must be a non-negative integer")
            elif model_key in model_assumptions:
                errors.append(f"duplicate assumption for {model_key}")
            else:
                model_assumptions[model_key] = value
        if len(assumption_ids) != len(set(assumption_ids)):
            errors.append("assumption ids must be unique")
        for model_key in expected_units:
            if model_key not in model_assumptions:
                errors.append(f"missing assumption for {model_key}")
            elif model_assumptions[model_key] != model[model_key]:
                errors.append(f"assumption does not match model.{model_key}")
    scenarios = data.get("scenarios")
    if not isinstance(scenarios, list) or len(scenarios) != 3:
        errors.append("exactly three scenarios are required")
    else:
        ids = [item.get("id") for item in scenarios if isinstance(item, dict)]
        if (
            len(ids) != len(scenarios)
            or any(not isinstance(item, str) for item in ids)
            or set(ids) != {"upside", "base", "downside"}
        ):
            errors.append("scenario ids must be upside, base, and downside")
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
                or not valid_date(scenario.get("effective_date"))
                or not isinstance(scenario.get("owner"), str)
                or not scenario["owner"].strip()
            ):
                errors.append(f"scenario {scenario.get('id', '?')} needs source, date, and owner")
            action = scenario.get("management_action")
            if not isinstance(action, str) or not action.strip():
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
