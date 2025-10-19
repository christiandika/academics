# Bike Rentals Analysis

This project performs **data cleaning, processing, analysis, and visualization** on a bike rental dataset.  
It is a simplified version of the original Jupyter notebook, converted into a single, easy-to-run Python script.

---

## 1. Overview

The script reads a CSV file containing daily and hourly bike rental data, standardizes the data format, processes numerical columns, performs grouping and encoding, and generates visualizations.

The output includes:
- Cleaned and processed CSV/JSON files
- Aggregated summary data
- Charts saved as `.png` images

---

## 2. Files

| File | Description |
|------|--------------|
| `bike_rentals_analysis_final.py` | Main Python script for data cleaning, processing, analysis, and visualization |
| `FloridaBikeRentals_Curated.csv` | Input dataset (must be present at the path defined in the script) |
| `README.md` | This documentation file |

---

## 3. Prerequisites

You need **Python 3.12 or later** and the following libraries:

```bash
pip install pandas numpy matplotlib scikit-learn
```

---

## 4. Configuration

At the top of the Python script, set your local file paths:

```python
BIKE_RENTAL_CSV_FILE = r"C:\Users\chris\OneDrive\programming\academics\bike_rental\FloridaBikeRentals_Curated.csv"
OUTPUT_DIR = r"C:\Users\chris\OneDrive\programming\academics\bike_rental\outputs"
```

The script will automatically create the output folder if it does not exist.

---

## 5. How to Run

Run the script from a terminal or command prompt:

```bash
python bike_rentals_analysis_final.py
```

Once completed, check the `OUTPUT_DIR` folder for:
- `bike_rental_cleaned.json`
- `bike_rental_processed.csv`
- `Rental_Bike_Data_Dummy.csv`
- Generated charts (`.png` files)

---

## 6. Main Steps in the Script

1. **Task 1 – Import & Clean**
   - Standardizes date formats (MM/DD/YYYY)
   - Checks for missing and duplicate values
   - Exports a cleaned JSON file

2. **Task 2 – Processing & Statistics**
   - Scales and converts selected numeric columns
   - Normalizes visibility data
   - Saves the processed dataset as a CSV

3. **Task 3 – Pandas Analysis**
   - Adds a `day_of_week` column
   - Filters by functioning days
   - Encodes categorical columns

4. **Task 4 – Visualizations**
   - Generates:
     - Bar chart of average rentals by season
     - Line chart of hourly rentals
     - Correlation heatmap

---

## 7. Output Examples

After running, your `outputs` folder will contain:

```
outputs/
│
├── bike_rental_cleaned.json
├── bike_rental_processed.csv
├── Rental_Bike_Data_Dummy.csv
├── avg_rentals_by_season.png
├── hourly_rentals.png
└── correlations_heatmap.png
```

---

## 8. Notes

- The dataset path must be valid and point directly to the CSV file.
- The script does not take command-line arguments.
- All paths use Python’s `pathlib` module for cross-platform compatibility.

---

**Author:** Christian Dika  
**Python Version:** 3.12.10  
**Last Updated:** October 2025
