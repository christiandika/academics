# Predicting Entry-Level Salary from Education & Career Data

This project explores whether academic and demographic features can predict **starting salaries** for recent graduates. It performs data cleaning, feature engineering, outlier handling, and regression modeling using multiple algorithms. The code was developed based on the dataset below and documented in the associated notebook.

---

## Source Data

- **Dataset:** [`education-and-career-success`](https://www.kaggle.com/datasets/adilshamim8/education-and-career-success)
- **Local file used:** `education_career_success.csv`
- **Notebook:** `predict_entry_salary.ipynb`
- **Goal:** Predict `starting_salary` (in USD) using education and aptitude-related features such as GPA, SAT score, university ranking, and field of study.

---

## Data Preparation

1. Dropped non-predictive fields (IDs, satisfaction, promotions, etc.).  
2. Identified and removed **12 upper outliers** with salaries above 90,950 USD (IQR method).  
3. Converted salary to **thousands** to normalize scale.  
4. Removed gender category “Other” and encoded gender as binary (`is_male`).  
5. One-hot encoded `field_of_study` (drop first).  
6. Applied **MinMaxScaler** to normalize numerical features.  
7. Split data into training (80%) and testing (20%) sets.

---

## Modeling Techniques

The notebook trained and evaluated the following regression models:

- Linear Regression  
- Polynomial Regression (degree = 2)  
- Lasso and LassoCV  
- Ridge and RidgeCV  
- Decision Tree Regressor

Each model’s performance was measured with **MSE**, **MAE**, **RMSE**, and **R²** on train and test sets.

---

## Key Results

- All linear and regularized models yielded **R² ≈ 0**, indicating **no predictive power**.  
- Decision Tree achieved **R²_train = 1.0** but **R²_test < 0**, showing severe **overfitting**.  
- Overall, models performed **worse than predicting the mean salary**.

---

## Conclusion (from original analysis)

The models did not successfully explain the variation in entry-level salaries using the available predictors. While academic performance and institutional ranking were expected to play a role, none of the features demonstrated a statistically significant relationship with salary outcomes. This indicates that **external factors such as geographic location, industry demand, employer reputation, negotiation skills, and internship quality likely dominate salary differences**.

In practical terms, this dataset is useful for educational analytics but not sufficient for salary forecasting. For better predictions, more diverse real-world attributes must be included.

---

## Quick Start

1. Place `education_career_success.csv` in the same directory.  
2. Install required dependencies:

   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

3. Run the Jupyter notebook:

   ```bash
   jupyter notebook predict_entry_salary.ipynb
   ```

---

## Files

- `predict_entry_salary.ipynb` — Jupyter Notebook with code and results  
- `education_career_success.csv` — Kaggle dataset used as input  

---
