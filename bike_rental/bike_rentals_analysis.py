#!/usr/bin/env python3
"""
Bike Rentals – Simplified Script (Explicit CSV path)

Usage:
- Update BIKE_RENTAL_CSV_FILE with the full path to your CSV file.
- Update OUTPUT_DIR with the folder where results and plots should be saved.
- Run this script directly (Python 3.12+ recommended).

Example:
  python bike_rentals_analysis.py
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# =========================
# User-configurable paths
# =========================
# Provide the FULL path to the CSV file
BIKE_RENTAL_CSV_FILE: str = r"C:\Users\chris\OneDrive\programming\academics\bike_rental\FloridaBikeRentals_Curated.csv"

# Folder where outputs will be written
OUTPUT_DIR: str = r"C:\Users\chris\OneDrive\programming\academics\bike_rental\outputs"


# -----------------------------
# Helpers for date conversion
# -----------------------------
EU_FORMAT_DATE_DASHES = "%d-%m-%Y"
US_FORMAT_DATE_SLASHES = "%m/%d/%Y"


def is_eu_date_with_dashes(date_input: str) -> bool:
    """Return True if value matches 'DD-MM-YYYY'."""
    try:
        datetime.strptime(date_input, EU_FORMAT_DATE_DASHES)
        return True
    except (ValueError, TypeError):
        return False


def is_us_date_with_slashes(date_input: str) -> bool:
    """Return True if value matches 'MM/DD/YYYY'."""
    try:
        datetime.strptime(date_input, US_FORMAT_DATE_SLASHES)
        return True
    except (ValueError, TypeError):
        return False


def to_us_date_with_slashes(date_input: str) -> str:
    """Convert any known date formats to MM/DD/YYYY."""
    if is_us_date_with_slashes(date_input):
        d = datetime.strptime(date_input, US_FORMAT_DATE_SLASHES)
        return d.strftime(US_FORMAT_DATE_SLASHES)
    if is_eu_date_with_dashes(date_input):
        d = datetime.strptime(date_input, EU_FORMAT_DATE_DASHES)
        return d.strftime(US_FORMAT_DATE_SLASHES)
    return "UnpredictedDateFormat"


# -----------------------------
# Core workflow functions
# -----------------------------
def load_data(csv_path: Path) -> pd.DataFrame:
    """Read the CSV into a DataFrame."""
    print(f"Loading data from: {csv_path}")
    return pd.read_csv(csv_path)


def task1_import_and_clean(df: pd.DataFrame, outdir: Path) -> pd.DataFrame:
    """Clean and standardize dataset."""
    print("TASK 1 — Import & Clean")

    if "date" in df.columns:
        df["date"] = df["date"].apply(to_us_date_with_slashes)
        bad_dates = (df["date"] == "UnpredictedDateFormat").sum()
        if bad_dates:
            print(f"  WARNING: {bad_dates} rows had unexpected date formats.")

    print("\nData snapshot:")
    print(df.head())
    print("\nMissing values per column:")
    print(df.isnull().sum())

    dups = df.duplicated().sum()
    if dups:
        print(f"  Found {dups} duplicate rows (not dropped).")

    cleaned_json = outdir / "bike_rental_cleaned.json"
    df.to_json(cleaned_json, orient="records", lines=True)
    print(f"  Saved cleaned JSON -> {cleaned_json}")
    return df


def task2_processing_and_stats(df: pd.DataFrame, source_csv: Path, outdir: Path) -> pd.DataFrame:
    """Process columns, compute stats, and save CSV."""
    print("\nTASK 2 — Processing & Statistics")

    for col in ["temp_celcius", "wind_speed_m_per_s", "dew_point_temp_celcius"]:
        if col in df.columns:
            df[col] = (df[col] * 10).astype("Int64")
            print(f"  Converted {col} -> scaled by 10 and cast to Int64")

    if "visibility_10m" in df.columns:
        scaler = MinMaxScaler()
        df["visibility_10m"] = scaler.fit_transform(df[["visibility_10m"]])
        print("  Scaled visibility_10m to [0, 1]")

    processed_csv = outdir / "bike_rental_processed.csv"
    df.to_csv(processed_csv, index=False)
    print(f"  Saved processed CSV -> {processed_csv}")
    return df


def task3_pandas_analysis(df: pd.DataFrame, outdir: Path) -> pd.DataFrame:
    """Perform groupings, add day_of_week, encode categoricals."""
    print("\nTASK 3 — Pandas Analysis")

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], format=US_FORMAT_DATE_SLASHES, errors="coerce")
        df["day_of_week"] = df["date"].dt.day_name()

    if "functioning_day" in df.columns:
        df = df[df["functioning_day"] == "Yes"].copy()
        print("  Filtered to functioning_day == 'Yes'")

    if "holiday" in df.columns:
        df["holiday_code"] = df["holiday"].map({"Holiday": 1, "No Holiday": 0}).astype("Int64")
    if "functioning_day" in df.columns:
        df["functioning_day_code"] = df["functioning_day"].map({"Yes": 1, "No": 0}).astype("Int64")
    if "seasons" in df.columns:
        df["seasons_code"] = df["seasons"].astype("category").cat.codes.astype("Int64")

    dummy_csv = outdir / "Rental_Bike_Data_Dummy.csv"
    df.to_csv(dummy_csv, index=False)
    print(f"  Saved dummy CSV -> {dummy_csv}")
    return df


def task4_visualizations(df: pd.DataFrame, outdir: Path) -> None:
    """Generate and save plots."""
    print("\nTASK 4 — Visualizations")

    if set(["seasons", "rented_bike_count"]).issubset(df.columns):
        avg_by_season = df.groupby("seasons")["rented_bike_count"].mean()
        plt.bar(avg_by_season.index, avg_by_season.values)
        plt.title("Average Rentals by Season")
        plt.ylabel("Average Rented Bikes")
        plt.xlabel("Season")
        plt.tight_layout()
        plt.savefig(outdir / "avg_rentals_by_season.png")
        plt.close()

    if set(["hour", "rented_bike_count"]).issubset(df.columns):
        hourly = df.groupby("hour")["rented_bike_count"].mean()
        plt.plot(hourly.index, hourly.values, marker="o")
        plt.title("Hourly Rentals")
        plt.xlabel("Hour")
        plt.ylabel("Average Rented Bikes")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(outdir / "hourly_rentals.png")
        plt.close()

    print("  Plots saved successfully.")


def main() -> None:
    csv_path = Path(BIKE_RENTAL_CSV_FILE)
    outdir = Path(OUTPUT_DIR)
    outdir.mkdir(parents=True, exist_ok=True)

    df = load_data(csv_path)
    df = task1_import_and_clean(df, outdir)
    df = task2_processing_and_stats(df, csv_path, outdir)
    df = task3_pandas_analysis(df, outdir)
    task4_visualizations(df, outdir)

    print("\nAll tasks completed. Outputs in:", outdir.resolve())


if __name__ == "__main__":
    main()