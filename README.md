# 🎓 Student Academic Performance & Risk Prediction

A machine learning project that predicts student academic performance and identifies students who may require additional academic support.

## 📌 Project Overview

Educational institutions can use academic and behavioral information to identify students who may be at risk of poor academic performance.

This project uses machine learning to:

* Analyze student academic and behavioral data
* Predict final academic performance
* Classify students as **At Risk** or **Not At Risk**
* Compare multiple machine learning models
* Provide an interactive Streamlit prediction interface

## 🎯 Objectives

* Perform data cleaning and exploratory data analysis
* Identify important factors associated with academic performance
* Build regression models for predicting final grades
* Build classification models for academic-risk detection
* Handle class imbalance
* Evaluate models using multiple performance metrics
* Build a simple web application for predictions

## 📊 Dataset

The project uses the **UCI Student Performance Dataset**.

The dataset contains information related to:

* Student demographics
* Family background
* Study time
* Previous failures
* Absences
* Academic support
* Social activities
* Health
* Other behavioral and educational factors

The target variable for grade prediction is:

`G3` — final grade.

For the academic-risk classification task, the project defines:

* `G3 < 10` → **At Risk**
* `G3 >= 10` → **Not At Risk**

This threshold is a project-defined rule and should not be interpreted as a universal definition of academic risk.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Imbalanced-learn
* Joblib
* Streamlit
* Google Colab

## 🔍 Exploratory Data Analysis

The project includes analysis of:

* Final grade distribution
* Study time vs final grade
* Previous failures vs final grade
* Absences vs final grade
* Feature correlations
* Correlation heatmap
* Random Forest feature importance

Some numerical relationships observed in the dataset included a negative relationship between previous failures and final grade and a positive relationship between study time and final grade.

Correlation describes association and does not establish causation.

## 🤖 Regression Models

The following regression models were evaluated:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor

### Regression Results

| Model             |   MAE |  RMSE |     R² |
| ----------------- | ----: | ----: | -----: |
| Linear Regression | 2.156 | 2.862 |  0.160 |
| Decision Tree     | 2.462 | 3.312 | -0.125 |
| Random Forest     | 2.057 | 2.815 |  0.187 |

The Random Forest Regressor produced the strongest results among the evaluated regression models on the selected test split.

## 🚨 Academic Risk Classification

Several classification approaches were evaluated:

* Random Forest
* Balanced Random Forest
* SMOTE Random Forest
* Balanced Logistic Regression

Because the dataset contains fewer At Risk students than Not At Risk students, accuracy alone was not considered sufficient.

The project therefore evaluates:

* Accuracy
* Precision
* Recall
* F1-score

### Cross-Validation Results

Stratified 5-fold cross-validation was used.

| Model                        | Accuracy | At Risk Precision | At Risk Recall | At Risk F1 |
| ---------------------------- | -------: | ----------------: | -------------: | ---------: |
| Random Forest                |   85.21% |            50.50% |            13% |      0.205 |
| Balanced Random Forest       |   85.06% |            58.77% |            22% |      0.305 |
| Balanced Logistic Regression |   76.58% |            35.64% |            67% |      0.463 |

The results demonstrate a trade-off between overall accuracy and detecting students classified as At Risk.

Balanced Logistic Regression produced the highest At Risk recall and F1-score in the cross-validation experiment, while Random Forest produced higher overall accuracy.

## 🧠 Final Risk Prediction Model

The final prototype uses a balanced Logistic Regression model for risk prediction because the project's primary objective is to identify students who may require academic support.

The model uses academic, demographic, behavioral, and social features while excluding `G1` and `G2` from the risk model to reduce target leakage.

## 🌐 Streamlit Application

The project includes a Streamlit web application where users can enter student information and receive:

* Predicted academic risk
* At Risk probability
* Academic-support recommendation

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Ashishcoder01/student-academic-performance-prediction.git
```

### 2. Open the project

```bash
cd student-academic-performance-prediction
```

### 3. Create a virtual environment

```bash
py -3.13 -m venv .venv
```

### 4. Activate the environment

Windows CMD:

```bash
.venv\Scripts\activate.bat
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

## 📁 Project Structure

```text
student-academic-performance-prediction/
│
├── app.py
├── student_risk_model.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
├── notebooks/
│   └── student_performance_prediction.ipynb
│
└── images/
    ├── grade_distribution.png
    ├── correlation_heatmap.png
    └── model_comparison.png
```

## ⚠️ Limitations

* The dataset contains only 649 records.
* The At Risk class is relatively smaller than the Not At Risk class.
* Risk classification depends on the project-defined `G3 < 10` threshold.
* Model performance may differ on students from other institutions or populations.
* The predictions should be treated as decision-support information rather than a definitive assessment of a student's academic ability.
* The current model does not use live LMS or institutional data.

## 🔮 Future Improvements

* Integrate with an LMS through an authorized API
* Use continuously updated academic data
* Add attendance and assessment tracking
* Build an automated student-support alert system
* Experiment with XGBoost and other models
* Perform hyperparameter optimization
* Evaluate the system on a larger and more diverse dataset
* Add teacher/admin dashboards
* Deploy the application online

## 👨‍💻 Author

**Ashish**

BTech CSE (AI-ML)
Galgotias University

### Skills Demonstrated

`Python` `Machine Learning` `Pandas` `NumPy` `Scikit-learn` `SQL` `Streamlit` `Data Analysis`

## ⭐ Project

If you find this project useful, consider giving the repository a star.
