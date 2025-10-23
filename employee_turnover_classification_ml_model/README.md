# Employee Turnover Prediction (HR Analytics)

Predict employee turnover (who is likely to leave) using classic HR features. This folder contains a Jupyter notebook with EDA, class-imbalance handling, multiple classification models, and a simple risk segmentation based on predicted probabilities.

## Files

- `employee_turnover.ipynb` — End-to-end analysis and modeling notebook.
- `HR_comma_sep.csv` — HR dataset used in the notebook (15,000 rows, header on row 1).

## Dataset

- Target: `left` (1 = employee left, 0 = stayed)
- Columns:
  - Numerical: `satisfaction_level`, `last_evaluation`, `number_project`, `average_montly_hours`, `time_spend_company`
  - Binary indicator: `Work_accident`, `promotion_last_5years`
  - Categorical: `department`, `salary`
- Basic preprocessing performed in the notebook:
  - One-hot encoding for `department` (drop_first=True)
  - Ordinal mapping for `salary`: {low: 0, medium: 1, high: 2}
  - Duplicate removal, null checks

## What the notebook does

1. Load and inspect data (shape, info, describe)
2. EDA
   - Correlation matrix of numeric features
   - Distribution plots for key features split by `left`
   - Category counts and relationships (e.g., projects vs left)
3. Clustering (KMeans)
   - Illustrative clustering using `satisfaction_level` and `last_evaluation` (not used for prediction)
4. Train/test split and class imbalance handling
   - 80/20 split with `random_state=123`
   - SMOTE applied on the training set to balance the `left` classes
5. Modeling (with 5-fold Stratified CV scored on recall)
   - Logistic Regression
   - Random Forest Classifier
   - Gradient Boosting Classifier
   - Metrics computed: Accuracy, Precision, Recall, F1, ROC AUC, optimal threshold via Youden’s J; ROC curve plotted
6. Model selection and insights
   - Random Forest selected as the best model by ROC AUC (and strong overall metrics)
   - Emphasis on Recall to minimize false negatives (i.e., reduce risk of missing likely leavers)
7. Risk segmentation for retention strategy
   - Convert predicted probabilities (from the selected model) into risk zones:
     - < 0.20 → Safe (Green)
     - 0.20–0.60 → Low Risk (Yellow)
     - 0.60–0.90 → Medium Risk (Orange)
     - ≥ 0.90 → High Risk (Red)
   - Visualize the distribution across zones and outline possible retention actions

## How to run

Prerequisites:
- Python 3.9–3.11
- Jupyter (VS Code, JupyterLab, or classic Notebook)

Install dependencies (one-time):

```powershell
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn
```

Open and run the notebook:
- In VS Code: open `employee_turnover.ipynb`, select a Python kernel, and Run All
- Or use Jupyter Lab/Notebook to open and execute the cells sequentially

## Results

- All metrics and plots are generated within the notebook. See the sections:
  - “Perform 5-fold cross-validation model training and evaluate performance”
  - “Logistic regression”, “Random Forest Classifier”, “Gradient Boosting Classifier”
  - ROC curves with the optimal threshold marker and confusion matrices
- The Random Forest model achieved the best ROC AUC in this workflow; Recall is prioritized to minimize false negatives.

## Reproducibility Notes

- Deterministic seeds are used where relevant (e.g., `random_state=42/123`).
- SMOTE is applied only on the training split to avoid leakage.
- Categorical handling: `department` one-hot (drop-first), `salary` ordinal mapping.

## Project structure

```
employee_turnover_ml_model/
├── employee_turnover.ipynb
├── HR_comma_sep.csv
└── README.md  ← you are here
```

## Credits and licensing

- Dataset: Fullstack Academy

