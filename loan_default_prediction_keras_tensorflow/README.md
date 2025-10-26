# Loan Default Prediction (Keras/TensorFlow)

Binary classification to predict **loan default risk** using tabular credit data. Implements preprocessing, class imbalance handling with **SMOTE**, a feed‑forward **neural network** in Keras/TensorFlow, and evaluation with ROC/AUC and Youden’s J–optimized threshold.

---

## Files

- **Notebook:** `loan_default_prediction_keras_tensorflow.ipynb`
- **Data:** `loan_data.csv`

---

## Dataset & Features (after cleaning)

- Original columns include: `credit_policy`, `purpose`, `int_rate`, `installment`, `log_annual_inc`, `dti`, `fico`, `days_with_cr_line`, `revol_bal`, `revol_util`, `inq_last_6mths`, `delinq_2yrs`, `pub_rec`, `not_fully_paid`.  
- Steps:
  - **No nulls / duplicates** found.
  - One‑hot encode `purpose` (drop first).  
  - Drop **`int_rate`, `credit_policy`, `revol_util`** based on correlation and potential leakage.

---

## Modeling Pipeline

1. **Train/Test split** (80/20).  
2. **Scale** features with `StandardScaler` (MinMax tested).  
3. **SMOTE** on training set to balance classes.  
4. **Neural Network (Sequential)**  
   - Dense(128, relu) → Dense(64, relu) → Dense(1, sigmoid)  
   - Optimizer **Adam**; loss **binary_crossentropy**; metrics: **accuracy**, **Recall**.  
   - **EarlyStopping** and custom epoch logging.
5. **Evaluation**
   - Compute **ROC/AUC**; choose operating point via **Youden’s J** to convert probabilities → labels.  
   - Report Accuracy, Precision, Recall, F1 (train & test), AUC, optimal threshold.

**Observed metrics (example run):** Test Accuracy ≈ **0.74**, Test Recall ≈ **0.74**, AUC ≈ **0.61** (threshold ~0.602).

---

## Quick Start

```bash
pip install pandas numpy seaborn matplotlib scikit-learn imbalanced-learn tensorflow
jupyter notebook loan_default_prediction_keras_tensorflow.ipynb
```

---

## Conclusion

Columns dropped: int_rate, credit_policy, revol_util

Class imbalance handled using SMOTE

Model: Neural Network with 2 hidden layers (128 and 64 neurons)

The model is volatile, with high variance in accuracy and recall across
epochs and the results depend on the random parameters selected in the
beginning.

Attenpted different configurations:
### Scaler: StandardScaler vs MinMaxScaler
### Optimizer: Adam with different learning rates
### Epochs: 50, 100, 200, 500, 1000, 2000, 5000

I calculated the optimal threshold using Youden's J statistic. The default
threshold of 0.5 was not optimal for this model, as it resulted in a low recall
of 0.37.

Our objective was to achieve a recall of 0.8 or higher, but the model did not
meet this requirement.

The results here show a test recall and a test accuracy of 0.74 both
