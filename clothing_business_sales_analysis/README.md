# AAL Q4 Sales Analysis (Australia)

This repository contains a Python script that analyzes **AAL’s Q4 2020 apparel sales in Australia** to support the Sales & Marketing (S&M) team with data‑driven insights and a dashboard of visualizations. The exercise brief covers data wrangling, descriptive analysis, visualization (daily/weekly/monthly/quarterly), and a short report for decision‑making.


## Problem Overview

AAL (est. 2000) is a nationwide apparel brand serving all age groups. During a strong growth phase, leadership asked S&M to: (1) identify **states with highest revenue**, (2) design **programs for low‑revenue states**, and (3) analyze **Q4 sales state‑by‑state** to guide next‑year planning. The dataset is `AusApparalSales4thQrt2020.csv`. The required tasks are: **Data wrangling**, **Data analysis**, **Data visualization**, and **Report generation**.

---

## What the Script Does

The analysis script performs the following using Pandas/NumPy/Seaborn/Matplotlib/Plotly and scikit‑learn:

1. **Load & inspect data**
   - Reads `AusApparalSales4thQrt2020.csv` and prints schema, summary stats, and sample rows.
   - Checks missingness with `isna()`, `isnull()`, and `notna()` for `Date`, `Time`, `State`, `Group`, `Unit`, `Sales`.

2. **Feature engineering**
   - Converts `Date` to datetime; derives `Month`, ISO `Year_Week`, `Weekday`.
   - Builds helper field `Sales_Thousands = Sales / 1000`.

3. **Descriptive analysis & visuals (daily/weekly/monthly/quarterly)**
   - **State‑level** totals (pie and bar charts).
   - **Monthly** totals & units (bar charts).
   - **Weekly** totals & units (bar charts).
   - **By Month × State**, **Month × Group**, **Month × Time of day** (bar charts).
   - **Daily trend** (line charts overall and per‑month).
   - **Distributional views** (box plot for month/day).

4. **Data quality check (average price)**
   - Computes daily average price (`Sales_Thousands / Unit * 1000`); finds it is **constant (≈ 2500 AUD)** across days—flagged as a potential **data issue**.

5. **Light preprocessing for correlation view**
   - Applies **Min‑Max scaling** to `Sales` and **One‑Hot encodes** categorical columns, then plots a correlation heatmap.

6. **Final report cells**
   - Summarize observed ranges and patterns for sales/units, state rankings, and non‑influential factors (groups/time‑of‑day), and provide recommendations for S&M focus.

---

## Requirements

- Python **3.12+**
- Packages:
  - `pandas`, `numpy`
  - `matplotlib`, `seaborn`
  - `plotly` (for interactive scatter demo)
  - `scikit-learn` (for `MinMaxScaler`)

You can install everything via:

```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn
```

---

## Project Structure

```
.
├─ clothing_business_sales_analysis.ipynb   # Analysis & dashboard code
├─ clothing_business_sales_analysis.py
├─ AusApparalSales4thQrt2020.csv            # Input data (place in same folder)
└─ README.md                             
```

---

## How to Run

1. **Place the CSV** `AusApparalSales4thQrt2020.csv` in the same directory as the script.
2. Run the script:

```bash
python clothing_business_sales_analysis.py
```

The script will:
- Print dataset info and basic stats.
- Generate multiple figures (pie/bar/line/box/heatmap). Depending on your environment, charts will display in a window or inline (e.g., in Jupyter).

> Tip: If using Jupyter, you can copy the code into a notebook to interleave Markdown commentary and plots as the brief recommends.

---

## Key Outputs & Panels

- **State‑wise sales**: Identify high/low revenue states (e.g., VIC/NSW higher; TAS/NT/WA lower in this dataset).  
- **Monthly summary**: Totals and units for Oct/Nov/Dec; December tends to be highest in this data.
- **Weekly view**: Bar charts by ISO week.
- **Groups & time‑of‑day**: Group and time‑of‑day patterns are broadly similar; not strong drivers in this dataset.
- **Trend lines & distributions**: Daily sales lines and month/day box plot to assess spread/outliers.
- **Correlation heatmap** after scaling/encoding to visualize numeric relationships.

> **Data quality note:** Daily average price appears constant (~2500 AUD), which may indicate **missing granularity or data issues**. Treat with caution before causal conclusions.


## Recommendations (from this analysis)

1. **Focus incremental S&M budget on lower‑revenue states** (e.g., WA, NT, TAS in this sample), validate with additional data sources.  
2. **Segment‑agnostic approach**: Groups (Kids/Women/Men/Seniors) and **time‑of‑day** showed limited differentiation; broader promotions may be sufficient unless deeper SKU‑level data says otherwise.  
3. **Data quality follow‑up**: Investigate why the **average price** is constant over days—confirm SKU/pricing granularity and ensure no transformation artifact.

---

## Notes & Assumptions

- File name is expected to be exactly `AusApparalSales4thQrt2020.csv`; adjust path in the script if your file lives elsewhere.
- Visual output depends on your environment (IDE vs. Jupyter). For a true **“dashboard”** feel, run in Jupyter and interleave Markdown sections as requested in the brief.
