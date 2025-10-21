# Groceries Store Marketing Analysis

This project performs an **exploratory data analysis (EDA)** and **hypothesis testing** to identify key factors influencing customer acquisition, spending behavior, and campaign performance for a groceries store. The analysis follows the marketing mix framework (4 Ps: Product, Price, Place, Promotion), with data-driven insights presented through Python-based visualization and statistics.

> Implemented in: `groceries_store_marketing_analysis.ipynb`

---

## Problem Scenario

The marketing mix is a cornerstone concept for designing effective marketing strategies. It involves multiple dimensions—**Product**, **Price**, **Place**, and **Promotion**—which collectively define a company’s market performance.

In this project, the goal is to **analyze customer demographics, channel preferences, and promotional responses** to derive actionable insights for marketing strategy optimization.

---

## Objective

As a data scientist, your objective is to conduct **exploratory data analysis and hypothesis testing** to understand how various customer attributes (age, education, income, family status, etc.) and marketing initiatives (campaigns, channels, spending categories) affect customer acquisition and behavior.

---

## Dataset Description

The dataset includes multiple variables across four key marketing dimensions:

| Dimension | Description |
|------------|-------------|
| **People** | Demographics such as birth year, education, income, marital status |
| **Product** | Spending categories (wine, fruits, meat, fish, sweets, gold, etc.) |
| **Place** | Distribution channels (website, catalog, and in-store purchases) |
| **Promotion** | Marketing campaign details, outcomes, and complaint data |

> Input dataset: `marketing_campaign.csv` (or equivalent)

---

## Analysis Steps

1. **Data Import and Validation**
   - Load the dataset and check the correct import of `Dt_Customer`, `Income`, and other key columns.
   - Inspect data types and missing values.

2. **Missing Value Imputation**
   - Handle missing `Income` values.
   - Imputation logic: Customers with **similar education and marital status** tend to have comparable income levels on average.
   - Clean inconsistent category names in `Education` and `Marital_Status` fields.

3. **Feature Engineering**
   - Create derived variables:
     - `TotalChildren` = sum of `Kidhome` + `Teenhome`
     - `Age` = 2025 - `Year_Birth`
     - `TotalSpending` = sum of product-related expenditures
     - `TotalPurchases` = `NumWebPurchases` + `NumCatalogPurchases` + `NumStorePurchases`

4. **Exploratory Visualization**
   - Generate **box plots** and **histograms** to understand distributions and detect outliers.
   - Apply **outlier treatment** where necessary.
   - Produce **heatmaps** to show correlations among numeric variables.

5. **Encoding**
   - Apply **Ordinal Encoding** to ordered categorical variables (e.g., Education levels).
   - Apply **One-Hot Encoding** to nominal variables (e.g., Marital Status, Country).

6. **Hypothesis Testing**
   - **H1:** Older individuals prefer **in-store shopping** over online channels.
   - **H2:** Customers with children prefer **online shopping** due to time constraints.
   - **H3:** Physical store sales are **cannibalized** by other channels.
   - **H4:** The **United States** significantly outperforms other countries in total purchases.

7. **Visual Analyses**
   - Identify **top and low-performing products** by total spending.
   - Explore **relationship between age** and **last campaign acceptance rate**.
   - Determine the **country with the most campaign acceptances**.
   - Explore patterns between **number of children** and **total expenditure**.
   - Analyze **education levels** among customers who **lodged complaints** in the last 2 years.

---

## Tools and Libraries

- **Python 3.12+**
- **Libraries used:**
  - `pandas`, `numpy`
  - `matplotlib`, `seaborn`
  - `plotly` (optional for interactive visuals)
  - `scipy`, `statsmodels` (for hypothesis testing)
  - `sklearn` (for encoding and preprocessing)

Installation:

```bash
pip install pandas numpy matplotlib seaborn plotly scipy statsmodels scikit-learn
```

---

## How to Run

1. Open the notebook `groceries_store_marketing_analysis.ipynb` in **Jupyter Notebook**, **VS Code**, or **Google Colab**.
2. Ensure the dataset (e.g., `marketing_campaign.csv`) is in the same directory.
3. Execute the notebook cells sequentially to reproduce the analysis.

---

## Key Deliverables

| Output | Description |
|--------|-------------|
| **EDA Results** | Descriptive stats and distribution plots |
| **Heatmap** | Correlation between customer and marketing variables |
| **Box & Histogram Plots** | Visualization of spending and demographic spread |
| **Hypothesis Tests** | Statistical evidence supporting or rejecting assumptions |
| **Campaign Insights** | Drivers of campaign success, product and country-level trends |

---

## Insights and Recommendations

- **Customer Segmentation:** Tailor marketing efforts by **age, education, and family composition**.
- **Channel Optimization:** Validate whether **online convenience** outweighs **in-store experience** for specific segments.
- **Promotion Focus:** Strengthen campaigns targeting demographics with historically low acceptance rates.
- **Geographic Strategy:** Use country-level purchase data to allocate marketing budgets efficiently.
- **Data Hygiene:** Ensure consistent encoding and maintain updated records for reliable income imputation.
