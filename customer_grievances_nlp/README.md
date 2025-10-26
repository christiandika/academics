# Customer Grievance Process – Classification & Sentiment Analysis

## Overview

This project analyzes customer banking complaints, cleans and processes the text data, classifies them into business departments using machine learning models, and performs **sentiment analysis** to assess customer emotions.

It uses both **Random Forest** and **Deep Neural Network (DNN)** approaches for classification, and leverages **VADER Sentiment Analysis** to extract emotional tone from customer complaints.

---

## Project Structure

### 1. Prepare and Read the Data
- Import necessary libraries: `pandas`, `numpy`, `scikit-learn`, `tensorflow`, `nltk`, `seaborn`, etc.
- Load complaint data and product–department mappings from an Excel file.

### 2. Data Quality Checks & Fixing Missing Values
- Inspect dataset for missing values.
- Fill in missing department values using predefined mapping rules.
- Ignore null values in `state` and `zip` columns as they are not relevant.

### 3. Date Range Identification
- Determine minimum and maximum complaint dates for coverage.

### 4. Text Preprocessing
- Convert text to lowercase.
- Remove numbers, punctuation, stopwords, and extra spaces.
- Apply lemmatization with POS tagging to reduce words to their base forms.

### 5. Text Cleaning
- Apply preprocessing to all complaints.
- Generate both tokenized and combined text columns.

### 6. Feature Engineering (TF-IDF)
- Transform preprocessed complaint text into numerical vectors using TF-IDF.
- Limit features to the top 1000 most frequent terms.

### 7. Modeling – Department Classification
#### Random Forest Classifier
- Train on TF-IDF features.
- Achieves **Train Accuracy: 99.98%** and **Test Accuracy: 73.91%**.
- More robust and less prone to overfitting than DNN.

#### Deep Neural Network (DNN)
- Multi-layer architecture with dropout regularization.
- Overfitting observed; not reliable.

### 8. Sentiment Analysis
- Use `SentimentIntensityAnalyzer` to compute sentiment scores: Negative, Positive, Neutral, and Compound.
- Although the data represents complaints, some texts show positive sentiment (possibly constructive complaints or resolved issues).
- Negative sentiments dominate, as expected.

---

## Insights & Potential Business Use

- **Automatic Routing:** Classification helps route complaints to the correct department.
- **Sentiment Tracking:** Sentiment scores can be used to:
  1. Prioritize complaints based on sentiment intensity.
  2. Prevent escalation of negative sentiments.
  3. Reduce customer churn by proactively addressing negative feedback.
  4. Monitor changes in customer sentiment over time to evaluate service quality.
  5. Define KPIs for measuring customer service improvement.

---

## How to Run

1. The complaints file name must be: `banking_complaints_2023.xlsx`
2. Complaint sheet name: `complaints_banking_2023`
3. Product-department mapping sheet name: `department_of_product`
4. Place your dataset file in the working directory.
5. Run all cells in the notebook to execute the workflow.

---

## Technologies Used
- **Python Libraries:** pandas, numpy, scikit-learn, tensorflow, nltk, seaborn
- **Machine Learning Models:** Random Forest, Deep Neural Network
- **Sentiment Analysis Tool:** VADER SentimentIntensityAnalyzer

---

## Summary
This workflow enables **automatic complaint classification** and **sentiment-based prioritization** of banking grievances. It demonstrates how machine learning and NLP can enhance operational efficiency and customer satisfaction through proactive complaint management.
