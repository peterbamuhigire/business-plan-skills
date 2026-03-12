"""
scrape_metrics.py — Country economic metrics scraper for business-plan-skills.

Fetches ~100 key business-planning metrics per country from the World Bank API
(primary source) and country-specific statistical portals via BeautifulSoup
(supplementary source for indicators not available on World Bank).

Output:
  country-context/{country}/references/economic-metrics.csv     — latest snapshot
  country-context/{country}/references/economic-metrics-history.csv — append-only time series

Columns: category, metric, value, unit, data_date, source
History adds: scraped_date (ISO date of the scrape run)

Usage:
  python tools/scrape_metrics.py                    # all countries with SKILL.md
  python tools/scrape_metrics.py kenya              # single country
  python tools/scrape_metrics.py kenya uganda       # multiple countries

Requirements:
  pip install -r tools/requirements.txt
  (requests, pandas, beautifulsoup4, openpyxl, xlrd)

Portal scrapers implemented:
  - UBOS (Uganda Bureau of Statistics) — ubos.org/datasets/
  - NBS Tanzania — nbs.go.tz/statistics/topic/high-frequency-data
  - CBK Kenya — centralbank.go.ke/monthly-economic-indicators/
  - KNBS Kenya — knbs.or.ke/data-releases/
  - BoU Uganda — archive.bou.or.ug/bou/bou-downloads/statistics/
"""

import sys
import os
import time
import io
import zipfile
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime

# Add project root to path so we can import metrics_config
sys.path.insert(0, os.path.dirname(__file__))
from metrics_config import METRICS, COUNTRY_CONFIGS

# ── Path helpers ──────────────────────────────────────────────────────────────

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def output_path(country_key: str) -> str:
    return os.path.join(
        REPO_ROOT, "country-context", country_key, "references", "economic-metrics.csv"
    )


def history_path(country_key: str) -> str:
    return os.path.join(
        REPO_ROOT, "country-context", country_key, "references", "economic-metrics-history.csv"
    )


# ── World Bank API ────────────────────────────────────────────────────────────

WB_BASE = "https://api.worldbank.org/v2"
WB_DELAY = 0.3  # seconds between requests (polite rate limit)


def fetch_world_bank(iso3: str, indicator: str) -> tuple[str | None, str | None]:
    """
    Fetch the most recent non-null value for a World Bank indicator.

    Returns: (value_string, year_string) or (None, None) on failure.
    """
    url = f"{WB_BASE}/country/{iso3}/indicator/{indicator}?format=json&per_page=10&mrv=5"
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()

        # data[0] = metadata, data[1] = list of records
        if len(data) < 2 or not data[1]:
            return None, None

        for record in data[1]:
            if record.get("value") is not None:
                value = record["value"]
                # Round floats sensibly
                if isinstance(value, float):
                    value = round(value, 4)
                return str(value), str(record.get("date", ""))

        return None, None

    except requests.exceptions.RequestException as e:
        print(f"      WB API error ({indicator}): {e}")
        return None, None
    except (KeyError, IndexError, ValueError) as e:
        print(f"      WB parse error ({indicator}): {e}")
        return None, None


# ── Portal scraper (BeautifulSoup + Excel/CSV/ZIP) ───────────────────────────


class PortalScraper:
    """
    Generic statistical portal scraper.

    Supports three file types via the `file_type` parameter:
      "csv"   — decode bytes → StringIO → pd.read_csv()
      "excel" — BytesIO → pd.read_excel()  (requires openpyxl / xlrd)
      "zip"   — unzip in-memory, find first Excel/CSV inside, then as above
    """

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
                ),
                "Accept": (
                    "text/html,application/xhtml+xml,application/xml;q=0.9,"
                    "application/vnd.ms-excel,application/vnd.openxmlformats-"
                    "officedocument.spreadsheetml.sheet,*/*;q=0.8"
                ),
            }
        )

    def find_file_url(
        self,
        page_path: str,
        extensions: tuple = (".csv", ".xls", ".xlsx", ".zip"),
        link_text_contains: str | None = None,
        href_contains: str | None = None,
    ) -> str | None:
        """
        Scrape page_path and return the URL of the first matching download link.

        Priority filters (applied in order):
          1. link_text_contains — anchor text contains this string (case-insensitive)
          2. href_contains      — href attribute contains this string
          3. extensions         — href ends with one of these extensions (fallback)
        """
        target_url = urljoin(self.base_url, page_path)
        try:
            response = self.session.get(target_url, timeout=15)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            all_links = soup.find_all("a", href=True)

            # Filter 1: anchor text
            if link_text_contains:
                matches = [
                    a for a in all_links
                    if a.get_text() and link_text_contains.lower() in a.get_text().lower()
                ]
                if matches:
                    return urljoin(self.base_url, matches[0]["href"])

            # Filter 2: href substring
            if href_contains:
                matches = [
                    a for a in all_links
                    if href_contains.lower() in a["href"].lower()
                ]
                if matches:
                    return urljoin(self.base_url, matches[0]["href"])

            # Filter 3: extension match
            matches = [
                a for a in all_links
                if any(a["href"].lower().endswith(ext) for ext in extensions)
            ]
            if matches:
                return urljoin(self.base_url, matches[0]["href"])

            return None

        except requests.exceptions.RequestException as e:
            print(f"      Portal scrape error ({page_path}): {e}")
            return None

    def download_and_clean(
        self, file_url: str, file_type: str = "excel", sheet: int | str = 0
    ) -> pd.DataFrame | None:
        """
        Download file_url and return a cleaned pandas DataFrame.

        file_type: "csv" | "excel" | "zip"
        sheet: sheet name or 0-based index (for Excel only)
        """
        if not file_url:
            return None
        try:
            response = self.session.get(file_url, timeout=30)
            response.raise_for_status()
            content_bytes = response.content

            if file_type == "zip":
                # Unzip in-memory, find first Excel or CSV inside
                with zipfile.ZipFile(io.BytesIO(content_bytes)) as zf:
                    names = zf.namelist()
                    target = next(
                        (n for n in names if n.lower().endswith((".xlsx", ".xls"))),
                        next((n for n in names if n.lower().endswith(".csv")), None),
                    )
                    if not target:
                        print(f"      No usable file in ZIP: {names}")
                        return None
                    content_bytes = zf.read(target)
                    file_type = "excel" if target.lower().endswith((".xlsx", ".xls")) else "csv"

            if file_type == "excel":
                df = pd.read_excel(io.BytesIO(content_bytes), sheet_name=sheet)
            else:
                text = content_bytes.decode("utf-8", errors="replace")
                df = pd.read_csv(io.StringIO(text))

            # Standardise column names
            df.columns = (
                df.columns.str.strip()
                .str.lower()
                .str.replace(r"\s+", "_", regex=True)
                .str.replace("-", "_", regex=False)
                .str.replace(r"[^\w]", "", regex=True)
            )
            df = df.dropna(how="all", axis=1).dropna(how="all", axis=0)
            return df

        except Exception as e:
            print(f"      Download/parse error ({file_url}): {e}")
            return None


# ── Country-specific portal scrapers ─────────────────────────────────────────
# Each function: returns dict { metric_name: (value_str, data_date_str, source_str) }
# Uses PortalScraper; empty dict returned on any failure (WB API is the fallback).


def scrape_uganda_ubos(metrics_needed: list[str]) -> dict:
    """
    UBOS (Uganda Bureau of Statistics) — ubos.org/datasets/
    Searches for Excel Tables links (WordPress site).
    Targets CPI and IIP data tables.
    """
    results = {}
    scraper = PortalScraper("https://www.ubos.org")

    # UBOS uploads Excel Tables for CPI on the datasets page
    file_url = scraper.find_file_url(
        "/datasets/",
        extensions=(".xls", ".xlsx"),
        link_text_contains="Excel Tables",
    )
    if not file_url:
        print("      UBOS: no Excel Tables link found on /datasets/")
        return results

    df = scraper.download_and_clean(file_url, file_type="excel")
    if df is None:
        return results

    # UBOS CPI table typically has Year/Month + CPI column
    # Try to extract headline inflation
    cpi_cols = [c for c in df.columns if "cpi" in c or "inflation" in c or "price" in c]
    if cpi_cols:
        latest = df.dropna(subset=[cpi_cols[0]]).iloc[-1]
        period = str(latest.get("year", latest.get("month", "latest")))
        results["Inflation rate, CPI (%)"] = (str(latest[cpi_cols[0]]), period, "UBOS")

    return results


def scrape_uganda_bou(metrics_needed: list[str]) -> dict:
    """
    Bank of Uganda — archive.bou.or.ug/bou/bou-downloads/statistics/
    Targets Monetary and Macroeconomic Indicators Excel file.
    """
    results = {}
    scraper = PortalScraper("https://archive.bou.or.ug")

    file_url = scraper.find_file_url(
        "/bou/bou-downloads/statistics/",
        extensions=(".xls", ".xlsx"),
        href_contains="Monetary",
    )
    if not file_url:
        # Fallback: any Excel in the statistics directory
        file_url = scraper.find_file_url(
            "/bou/bou-downloads/statistics/",
            extensions=(".xls", ".xlsx"),
        )
    if not file_url:
        print("      BoU: no Excel file found in statistics directory")
        return results

    df = scraper.download_and_clean(file_url, file_type="excel")
    if df is None:
        return results

    # BoU file structure varies — try to find lending rate and CBR
    rate_cols = [c for c in df.columns if "lend" in c or "cbr" in c or "rate" in c]
    if rate_cols:
        latest = df.dropna(subset=[rate_cols[0]]).iloc[-1]
        period = str(latest.get("date", latest.get("period", "latest")))
        results["Lending interest rate (%)"] = (str(latest[rate_cols[0]]), period, "Bank of Uganda")

    return results


def scrape_kenya_cbk(metrics_needed: list[str]) -> dict:
    """
    Central Bank of Kenya — centralbank.go.ke/monthly-economic-indicators/
    Looks for Monthly Economic Indicators link (WordPress; may be ZIP or Excel).
    """
    results = {}
    scraper = PortalScraper("https://www.centralbank.go.ke")

    # Try to find the most recent Monthly Economic Indicators file
    file_url = scraper.find_file_url(
        "/monthly-economic-indicators/",
        extensions=(".xlsx", ".xls", ".zip"),
        link_text_contains="Monthly Economic Indicators",
    )
    if not file_url:
        file_url = scraper.find_file_url(
            "/monthly-economic-indicators/",
            extensions=(".xlsx", ".xls", ".zip"),
        )
    if not file_url:
        print("      CBK: no file found on /monthly-economic-indicators/")
        return results

    # Determine whether ZIP or Excel
    file_type = "zip" if file_url.lower().endswith(".zip") else "excel"
    df = scraper.download_and_clean(file_url, file_type=file_type)
    if df is None:
        return results

    # CBK file: look for lending rate, CBR, inflation columns
    mapping = {
        "Lending interest rate (%)": ["lending", "commercial_bank_rate", "average_lending"],
        "Inflation rate, CPI (%)": ["inflation", "cpi", "headline"],
        "Deposit interest rate (%)": ["deposit", "savings"],
    }
    for metric_name, search_terms in mapping.items():
        if metric_name not in metrics_needed:
            continue
        col = next((c for c in df.columns if any(t in c for t in search_terms)), None)
        if col:
            latest = df.dropna(subset=[col]).iloc[-1]
            period = str(latest.get("date", latest.get("month", "latest")))
            results[metric_name] = (str(latest[col]), period, "CBK Monthly Economic Indicators")

    return results


def scrape_kenya_knbs(metrics_needed: list[str]) -> dict:
    """
    KNBS — knbs.or.ke/data-releases/
    Uses WordPress download manager — links are /?wpdmdl=XXXX format.
    Searches by anchor text for CPI / GDP data releases.
    """
    results = {}
    scraper = PortalScraper("https://www.knbs.or.ke")

    # KNBS download manager: search by link text containing "CPI" or "Economic Indicators"
    for search_term, metric_name in [
        ("CPI", "Inflation rate, CPI (%)"),
        ("GDP", "Real GDP growth rate (%)"),
    ]:
        if metric_name not in metrics_needed:
            continue
        file_url = scraper.find_file_url(
            "/data-releases/",
            href_contains="wpdmdl",
            link_text_contains=search_term,
        )
        if not file_url:
            continue

        # KNBS files are Excel
        df = scraper.download_and_clean(file_url, file_type="excel")
        if df is None:
            continue

        # Try to extract most recent value
        val_col = next(
            (c for c in df.columns if search_term.lower() in c or "rate" in c or "index" in c),
            None,
        )
        if val_col:
            latest = df.dropna(subset=[val_col]).iloc[-1]
            period = str(latest.get("year", latest.get("period", "latest")))
            results[metric_name] = (str(latest[val_col]), period, "KNBS Data Release")

    return results


def scrape_tanzania_nbs(metrics_needed: list[str]) -> dict:
    """
    NBS Tanzania — nbs.go.tz/statistics/topic/high-frequency-data
    Joomla site; data files as .xls/.xlsx in article body.
    """
    results = {}
    scraper = PortalScraper("https://www.nbs.go.tz")

    file_url = scraper.find_file_url(
        "/statistics/topic/high-frequency-data",
        extensions=(".xls", ".xlsx"),
    )
    if not file_url:
        print("      NBS Tanzania: no Excel file found on high-frequency-data page")
        return results

    df = scraper.download_and_clean(file_url, file_type="excel")
    if df is None:
        return results

    # NBS high-frequency data: look for GDP, inflation, exchange rate columns
    mapping = {
        "Real GDP growth rate (%)": ["gdp", "real_gdp", "growth"],
        "Inflation rate, CPI (%)": ["inflation", "cpi", "headline"],
        "Exchange rate TZS/USD": ["exchange", "usd", "tzs"],
    }
    for metric_name, terms in mapping.items():
        if metric_name not in metrics_needed:
            continue
        col = next((c for c in df.columns if any(t in c for t in terms)), None)
        if col:
            latest = df.dropna(subset=[col]).iloc[-1]
            period = str(latest.get("date", latest.get("year", "latest")))
            results[metric_name] = (str(latest[col]), period, "NBS Tanzania High Frequency Data")

    return results


# Map country key → list of portal scraper functions
PORTAL_SCRAPERS: dict[str, list] = {
    "uganda": [scrape_uganda_ubos, scrape_uganda_bou],
    "kenya": [scrape_kenya_cbk, scrape_kenya_knbs],
    "tanzania": [scrape_tanzania_nbs],
}


# ── Core scrape routine ───────────────────────────────────────────────────────


def scrape_country(country_key: str) -> pd.DataFrame:
    """
    Fetch all 100 metrics for a country.
    Priority: World Bank API → country portal scrapers → leave blank.

    Returns a DataFrame with columns:
      category, metric, value, unit, data_date, source
    """
    config = COUNTRY_CONFIGS.get(country_key)
    if not config:
        print(f"  No config found for '{country_key}'. Skipping.")
        return pd.DataFrame()

    iso3 = config["iso3"]
    display = config["display_name"]
    print(f"\n{'='*60}")
    print(f"  Scraping {display} ({iso3})")
    print(f"{'='*60}")

    # Step 1: collect any portal-scraped supplements first (cheap, no rate limit)
    portal_data: dict = {}
    for scraper_fn in PORTAL_SCRAPERS.get(country_key, []):
        try:
            portal_data.update(scraper_fn([m["name"] for m in METRICS]))
        except Exception as e:
            print(f"  Portal scraper error ({scraper_fn.__name__}): {e}")

    # Step 2: iterate metrics
    rows = []
    for idx, metric in enumerate(METRICS, start=1):
        name = metric["name"]
        category = metric["category"]
        indicator = metric["indicator"]
        unit = metric["unit"]
        default_source = metric["source"]

        value, data_date, source = None, None, default_source

        # 2a. Try World Bank API
        if indicator:
            wb_value, wb_date = fetch_world_bank(iso3, indicator)
            if wb_value is not None:
                value = wb_value
                data_date = wb_date
                print(f"  [{idx:>3}] ✓  {name[:55]:<55} {value} ({data_date})")
            else:
                print(f"  [{idx:>3}] –  {name[:55]:<55} (no WB data)")
            time.sleep(WB_DELAY)

        # 2b. Fall back to portal data
        if value is None and name in portal_data:
            portal_value, portal_date, portal_source = portal_data[name]
            value = portal_value
            data_date = portal_date
            source = portal_source
            print(f"  [{idx:>3}] ✓P {name[:55]:<55} {value} ({data_date}) [{source}]")

        # 2c. Leave blank if still nothing
        if value is None:
            value = ""
            data_date = ""

        rows.append(
            {
                "category": category,
                "metric": name,
                "value": value,
                "unit": unit,
                "data_date": data_date,
                "source": source,
            }
        )

    return pd.DataFrame(rows)


# ── CSV writer ─────────────────────────────────────────────────────────────────


def save_metrics_csv(df: pd.DataFrame, country_key: str) -> str:
    """
    Write two files:
      1. economic-metrics.csv        — latest snapshot (overwritten each run)
      2. economic-metrics-history.csv — append-only time series for trend analysis

    The history file adds a 'scraped_date' column (ISO date of this run) so
    Claude can compare values across scrape dates when generating a business plan.
    """
    path = output_path(country_key)
    hist = history_path(country_key)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    run_date = datetime.now().strftime("%Y-%m-%d")

    # 1. Overwrite latest snapshot
    df.to_csv(path, index=False, encoding="utf-8")

    # 2. Append to history (prepend scraped_date column)
    df_hist = df.copy()
    df_hist.insert(0, "scraped_date", run_date)

    if os.path.exists(hist):
        df_hist.to_csv(hist, mode="a", header=False, index=False, encoding="utf-8")
    else:
        df_hist.to_csv(hist, index=False, encoding="utf-8")

    return path


# ── Main ──────────────────────────────────────────────────────────────────────


def main():
    started = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\nbusiness-plan-skills — metric scraper  [{started}]")
    print(f"Repo root: {REPO_ROOT}\n")

    # Determine which countries to scrape
    args = [a.lower() for a in sys.argv[1:]]
    if args:
        targets = [k for k in args if k in COUNTRY_CONFIGS]
        unknown = [k for k in args if k not in COUNTRY_CONFIGS]
        if unknown:
            print(f"Warning: unknown country keys: {', '.join(unknown)}")
            print(f"Configured countries: {', '.join(COUNTRY_CONFIGS.keys())}\n")
    else:
        # Only scrape countries that already have a SKILL.md
        targets = []
        for key in COUNTRY_CONFIGS:
            skill_path = os.path.join(REPO_ROOT, "country-context", key, "SKILL.md")
            if os.path.exists(skill_path):
                targets.append(key)
        print(f"Auto-detected countries with SKILL.md: {', '.join(targets)}")

    if not targets:
        print("No valid targets found. Exiting.")
        sys.exit(1)

    results = []
    for country_key in targets:
        df = scrape_country(country_key)
        if df.empty:
            results.append((country_key, 0, 0, "skipped"))
            continue

        total = len(df)
        filled = (df["value"] != "").sum()
        path = save_metrics_csv(df, country_key)
        results.append((country_key, filled, total, path))
        print(f"\n  Saved → {path}  ({filled}/{total} metrics populated)")

    # Summary
    print(f"\n{'='*60}")
    print("  SUMMARY")
    print(f"{'='*60}")
    for country_key, filled, total, path in results:
        if path == "skipped":
            print(f"  {country_key:<15}  SKIPPED")
        else:
            pct = round(filled / total * 100) if total else 0
            short_path = path.replace(REPO_ROOT + os.sep, "")
            print(f"  {country_key:<15}  {filled}/{total} ({pct}%)  → {short_path}")
    print()


if __name__ == "__main__":
    main()
