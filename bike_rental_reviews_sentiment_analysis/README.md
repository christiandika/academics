# Bike Rental Reviews Sentiment Analysis

## Project Overview

This project focuses on **sentiment analysis** of customer reviews for a bike rental service.  
The objective is to classify reviews into three categories: **positive**, **neutral**, or **negative**.

### Workflow
1. Import and prepare data  
2. Clean and preprocess text  
3. Convert text into numerical embeddings  
4. Train and evaluate multiple machine learning and deep learning models:
   - Logistic Regression  
   - Naïve Bayes  
   - LSTM (Bidirectional)  
   - BERT (pretrained transformer)

---

## Dataset

- **Source files:**  
  - `bike_rental_reviews.csv` (50,000 reviews)  
  - `bike_rental_reviews_augmented_unique.csv` (synthetic data)
- **Data processing summary:**
  - Removed 49,700 duplicate reviews, leaving **300 unique reviews** (100 per sentiment class).  
  - Added **synthetic reviews** for data balance, resulting in **3,300 total records**:  
    - 1,100 positive  
    - 1,100 neutral  
    - 1,100 negative  
- Both CSV files must be placed in the working directory for successful execution.

---

## Preprocessing Steps

Applied the following text preprocessing transformations:

- Convert to lowercase  
- Remove numbers  
- Remove stopwords (except key sentiment words such as *not*, *no*, *never*, *very*, *really*, *extremely*)  
- Remove punctuation and extra spaces  
- Tokenization and POS tagging  
- Lemmatization using **WordNet**
- Text converted into numerical vectors using **Word2Vec embeddings**.

---

## Models Implemented

### 1. Logistic Regression
- Achieved strong performance with approximately **90% accuracy** and **F1 score ≈ 0.90**.

### 2. Naïve Bayes
- Slightly lower accuracy (~86%), effective as a simple baseline model.

### 3. LSTM (Bidirectional)
- Configured with an embedding layer and bidirectional LSTM.
- Results were poor (**~33% accuracy**), likely due to limited data and insufficient hyperparameter tuning.

### 4. BERT (Transformers)
- Fine-tuned using `bert-base-uncased`.
- Achieved **~33% accuracy**, suggesting the need for further fine-tuning and more training data.

---

## Performance Summary

| Model                | Train Accuracy | Test Accuracy | Train F1 | Test F1 |
|----------------------|----------------|----------------|-----------|----------|
| Logistic Regression  | 0.9178         | 0.8985         | 0.9185    | 0.8991   |
| Naïve Bayes          | 0.8761         | 0.8636         | 0.8753    | 0.8633   |
| LSTM (Bidirectional) | 0.3333         | 0.3333         | 0.1667    | 0.1667   |
| BERT (Transformer)   | 0.3322         | 0.3379         | 0.1657    | 0.1707   |

---

## Dependencies

Make sure the following Python libraries are installed:

```bash
pip install pandas numpy matplotlib nltk scikit-learn tensorflow gensim transformers
```

---

## How to Run

1. Place the datasets `bike_rental_reviews.csv` and `bike_rental_reviews_augmented_unique.csv` in your working directory.  
2. Run the Python script or Jupyter Notebook (`bike_rental_reviews_sentiment_analysis.ipynb`).  
3. The script will:  
   - Load and preprocess data  
   - Train models  
   - Output evaluation metrics such as accuracy, F1 score, confusion matrix, and classification report

---

## Conclusion

Among all tested models:  
- **Logistic Regression** performed the best, with a **test accuracy of 89.9%** and **F1 score of 0.8991**.  
- **Naïve Bayes** followed closely with a **test accuracy of 86.4%** and **F1 score of 0.8633**.  
- **LSTM** and **BERT** significantly underperformed on this dataset, likely due to limited training data and hyperparameter tuning constraints.
