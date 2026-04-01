# Audio Classification using MFCC and Machine Learning

## Overview
This project builds an end-to-end audio classification system using MFCC (Mel-Frequency Cepstral Coefficients) and machine learning.

The model classifies environmental sounds into categories such as:
- dog_bark
- drilling
- siren
- street_music

---

## Dataset
We use a subset of the UrbanSound8K dataset:
- 4 classes
- ~100 samples per class
- Balanced dataset

---

## Methodology

### 1. Audio Loading
- Used `librosa` to load audio files
- Standardized audio length (4 seconds)

### 2. Feature Extraction
- Extracted MFCC features (13 coefficients)
- Aggregated using mean over time

### 3. Dataset Preparation
- Features stored in `X`
- Labels stored in `y`
- Train/Test split: 80/20

### 4. Model Training
- Random Forest Classifier
- Compared with SVM (optional)

### 5. Evaluation
- Accuracy: ~98.75%
- Confusion Matrix used for analysis

---

## Results

- High accuracy (~98%)
- Very low misclassification
- Strong performance across all classes

---

## Technologies Used

- Python
- Librosa
- NumPy
- Scikit-learn
- Matplotlib

---

## Project Structure
audio-classification-mfcc/
│
├── data/ # (ignored)
├── notebooks/ # Jupyter notebook
├── results/ # outputs
├── prepare_subset.py # dataset script
├── requirements.txt
└── README.md


---

## Future Improvements

- Use deep learning (CNN on spectrograms)
- Hyperparameter tuning
- Use full UrbanSound8K dataset

---

## Author

Muhammad Shoaib