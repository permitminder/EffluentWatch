#!/usr/bin/env python3
"""
EffluentWatch EPA ECHO Industry Code Fetcher

Downloads NPDES_NAICS.csv and NPDES_SICS.csv from the EPA ECHO ICIS-NPDES
bulk download, filters to Texas permits, keeps only primary codes,
and produces a lookup CSV: utils/permit_industry_lookup.csv

Data source:
  https://echo.epa.gov/tools/data-downloads/icis-npdes-download-summary

Requirements: requests, pandas
"""

import os
import sys
import tempfile
import zipfile
from datetime import datetime

import pandas as pd
import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ECHO_BASE_URL = "https://echo.epa.gov/files/echodownloads"
ZIP_FILENAME = "npdes_downloads.zip"
OUTPUT_FILE = "utils/permit_industry_lookup.csv"
TX_PREFIX = "TX"


# ---------------------------------------------------------------------------
# Download
# ---------------------------------------------------------------------------

def stream_download(url: str, dest_path: str) -> None:
    """Stream-download *url* to *dest_path*, printing progress."""
    print(f"  Downloading: {url}")
    resp = requests.get(url, stream=True, timeout=600)
    resp.raise_for_status()

    total = int(resp.headers.get("content-length", 0))
    downloaded = 0
    chunk_mb = 1 << 20  # 1 MB

    with open(dest_path, "wb") as fh:
        for chunk in resp.iter_content(chunk_size=chunk_mb):
            if chunk:
                fh.write(chunk)
                downloaded += len(chunk)
                if total:
                    pct = downloaded / total * 100
                    print(
                        f"\r  {downloaded / 1e6:.1f} MB / {total / 1e6:.1f} MB"
                        f" ({pct:.0f}%)",
                        end="",
                        flush=True,
                    )
    print()  # newline after progress


# ---------------------------------------------------------------------------
# Extract & filter
# ---------------------------------------------------------------------------

def extract_and_filter_tx(zip_path: str, csv_name: str, permit_col: str) -> pd.DataFrame:
    """
    Extract *csv_name* from the ECHO ZIP, filter to TX permits,
    and return the filtered DataFrame.
    """
    with zipfile.ZipFile(zip_path, "r") as zf:
        names = zf.namelist()
        match = next((n for n in names if n.lower() == csv_name.lower()), None)
        if not match:
            print(f"  Warning: {csv_name} not found in ZIP. Contents: {names[:10]}...")
            return pd.DataFrame()

        print(f"  Reading {match} ...")
        with zf.open(match) as fh:
            df = pd.read_csv(fh, dtype=str, low_memory=False)

    print(f"  Total rows: {len(df):,}")

    # Filter to TX permits
    if permit_col in df.columns:
        df[permit_col] = df[permit_col].str.strip().str.upper()
        df = df[df[permit_col].str.startswith(TX_PREFIX)].copy()
        print(f"  TX rows: {len(df):,}")
    else:
        print(f"  Warning: column '{permit_col}' not found. Columns: {list(df.columns)}")
        return pd.DataFrame()

    return df


def pick_primary(df: pd.DataFrame, permit_col: str, code_col: str, flag_col: str) -> pd.DataFrame:
    """
    For each permit, keep only the primary code. If no primary flag,
    fall back to the first row for that permit.
    """
    if df.empty:
        return df

    # Try to use primary indicator flag
    if flag_col in df.columns:
        primary = df[df[flag_col].str.strip().str.upper() == "Y"]
        if not primary.empty:
            # Take first primary per permit
            result = primary.drop_duplicates(subset=[permit_col], keep="first")
            # Add permits that have no primary flag
            missing_permits = set(df[permit_col]) - set(result[permit_col])
            if missing_permits:
                fallback = df[df[permit_col].isin(missing_permits)].drop_duplicates(
                    subset=[permit_col], keep="first"
                )
                result = pd.concat([result, fallback], ignore_index=True)
            return result

    # No flag column or no flagged rows — just take first per permit
    return df.drop_duplicates(subset=[permit_col], keep="first")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print(f"\n{'='*60}")
    print("EffluentWatch EPA ECHO Industry Code Fetcher")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")

    url = f"{ECHO_BASE_URL}/{ZIP_FILENAME}"

    with tempfile.TemporaryDirectory() as tmp_dir:
        zip_path = os.path.join(tmp_dir, ZIP_FILENAME)

        # --- Download ---
        try:
            stream_download(url, zip_path)
        except requests.HTTPError as exc:
            print(f"  HTTP {exc.response.status_code} — download failed.")
            sys.exit(1)
        except Exception as exc:
            print(f"  Download error: {exc}")
            sys.exit(1)

        # --- Extract NAICS ---
        print("\nProcessing NAICS codes ...")
        naics_df = extract_and_filter_tx(zip_path, "NPDES_NAICS.csv", "NPDES_ID")
        if not naics_df.empty:
            naics_df = pick_primary(naics_df, "NPDES_ID", "NAICS_CODE", "PRIMARY_INDICATOR_FLAG")
            # Keep only what we need
            naics_cols = {"NPDES_ID": "PERMIT_NUMBER"}
            if "NAICS_CODE" in naics_df.columns:
                naics_cols["NAICS_CODE"] = "NAICS_CODE"
            if "NAICS_DESC" in naics_df.columns:
                naics_cols["NAICS_DESC"] = "NAICS_DESC"
            elif "NAICS_DESCRIPTION" in naics_df.columns:
                naics_cols["NAICS_DESCRIPTION"] = "NAICS_DESC"
            naics_df = naics_df.rename(columns=naics_cols)[list(naics_cols.values())]
            print(f"  NAICS: {len(naics_df):,} TX permits with codes")
        else:
            naics_df = pd.DataFrame(columns=["PERMIT_NUMBER", "NAICS_CODE", "NAICS_DESC"])

        # --- Extract SIC ---
        print("\nProcessing SIC codes ...")
        sic_df = extract_and_filter_tx(zip_path, "NPDES_SICS.csv", "NPDES_ID")
        if not sic_df.empty:
            sic_df = pick_primary(sic_df, "NPDES_ID", "SIC_CODE", "PRIMARY_INDICATOR_FLAG")
            sic_cols = {"NPDES_ID": "PERMIT_NUMBER"}
            if "SIC_CODE" in sic_df.columns:
                sic_cols["SIC_CODE"] = "SIC_CODE"
            if "SIC_DESC" in sic_df.columns:
                sic_cols["SIC_DESC"] = "SIC_DESC"
            elif "SIC_DESCRIPTION" in sic_df.columns:
                sic_cols["SIC_DESCRIPTION"] = "SIC_DESC"
            sic_df = sic_df.rename(columns=sic_cols)[list(sic_cols.values())]
            print(f"  SIC: {len(sic_df):,} TX permits with codes")
        else:
            sic_df = pd.DataFrame(columns=["PERMIT_NUMBER", "SIC_CODE", "SIC_DESC"])

    # --- Merge NAICS + SIC on permit number ---
    print("\nMerging NAICS and SIC data ...")
    if naics_df.empty and sic_df.empty:
        print("ERROR: No industry codes found for TX permits. Exiting.")
        sys.exit(1)

    lookup = pd.merge(naics_df, sic_df, on="PERMIT_NUMBER", how="outer")
    lookup = lookup.fillna("")
    lookup = lookup.sort_values("PERMIT_NUMBER").reset_index(drop=True)

    # --- Save ---
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    lookup.to_csv(OUTPUT_FILE, index=False)
    print(f"\nSaved {len(lookup):,} permits to {OUTPUT_FILE}")

    # Stats
    has_sic = (lookup["SIC_CODE"] != "").sum() if "SIC_CODE" in lookup.columns else 0
    has_naics = (lookup["NAICS_CODE"] != "").sum() if "NAICS_CODE" in lookup.columns else 0
    print(f"  With SIC code:   {has_sic:,}")
    print(f"  With NAICS code: {has_naics:,}")

    print(f"\n{'='*60}")
    print("COMPLETE")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
