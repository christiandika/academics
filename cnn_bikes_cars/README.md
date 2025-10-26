# CNN: Bikes vs Cars Image Classification

A concise TensorFlow/Keras project that classifies **bikes** vs **cars** using a small image dataset and several CNN baselines/variants. The workflow includes data validation, preprocessing, augmentation, model training, and evaluation with ROC/AUC and Youden’s J statistic.

- **Notebook:** `cnn_bikes_cars.ipynb`

---

## Dataset & Prep (short)
- Classes: `bikes`, `cars`; roughly balanced (≈397 vs 400 images).
- Basic EDA on image sizes; no corrupted or extreme-ratio images detected.
- Train/Val/Test from directory with `image_dataset_from_directory`, `validation_split=0.2`, then 50/50 split of the temp validation for final **val**/**test**.
- Normalization via `layers.Rescaling(1./255)`. Data augmented with flips, small rotations, translations, and zooms.

---

## Models Trained
1) **Baseline (no augmentation)** – 3×Conv2D + MaxPool → Dense.  
2) **Baseline + augmentation** – same backbone preceded by `data_augmentation`.  
3) **Advanced: max & average pooling** – deeper CNN with BatchNorm + mixed pooling.  
4) **Advanced: max pooling only** – deeper CNN with BatchNorm + dropout.

**Common setup:** loss=`binary_crossentropy`, metric=`accuracy`, optimizer=Adam, `epochs=10`.

---

## Evaluation (high level)
- Metrics tracked: Accuracy (train/test), Precision, Recall, F1, AUC, optimal threshold (Youden’s J).  
- Utility functions compute ROC/AUC, confusion matrix, and display misclassified samples.

**Observed summary from runs:** the **Baseline + augmentation** variant yielded the best validation/test performance among the four models.

---

## Quick Start
```bash
pip install tensorflow matplotlib seaborn scikit-learn
jupyter notebook cnn_bikes_cars.ipynb
```
Place your `bikes/` and `cars/` subfolders under a single root directory and update the path in the notebook.

---

## Conclusion

**Dataset Summary**  
- Total images in original dataset: **797**  
- Training images: **633**  
- Validation images: **39**  
- Test images: **56**  
- Models tested: **4**  
- Epochs: **10**

**Results Summary**  
- The **Baseline Model with Data Augmentation** outperformed all others.  
  - **Best Test Accuracy:** 0.957  
  - **Best AUC:** 0.99  
- The advanced models performed **worse** than the baseline models, which was unexpected.

**Class-Level Observations**  
- The **bikes** class was generally more challenging, with more misclassifications than **cars** across models.  
- For the selected model, the **car** class became the challenging one, with only **4 misclassified images**.

**Patterns in Misclassified Car Images**  
1. The car is **obstructed** (e.g., by a pole).  
2. The image contains **multiple cars**, causing confusion.  
3. The image depicts **cars in traffic**, reducing clarity.  
4. The car appears in a **green landscape**, where the dark green background is similar to the car color.

**Model Behavior Notes**  
- Test metrics are **consistently better than training metrics**, suggesting potential model instability or data leakage — further investigation is required.