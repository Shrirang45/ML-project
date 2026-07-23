# 🎓 Student Performance Indicator

A Machine Learning project that predicts a student's **Math Score** based on demographic information, parental education, lunch type, test preparation course, and other academic scores.

---

## 📌 Project Overview

Student performance is influenced by several factors such as parental education, lunch type, gender, and test preparation.

This project performs Exploratory Data Analysis (EDA), Feature Engineering, Data Preprocessing, and trains multiple Machine Learning regression models to predict student performance.

---

## 📂 Project Structure

```
Student Performance Indicator/
│
├── notebooks/
│   ├── 1. EDA and Feature Engineering.ipynb
│   ├── 2. Model Training.ipynb
│   └── StudentsPerformance.csv
│
├── src/
│
├── requirements.txt
├── setup.py
├── README.md
└── .gitignore
```

---

## 📊 Dataset

The dataset contains information about students including:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch
- Test Preparation Course
- Reading Score
- Writing Score
- Math Score (Target)

---

## 🔍 Exploratory Data Analysis (EDA)

Performed:

- Dataset inspection
- Missing value check
- Duplicate value check
- Feature type identification
- Statistical summary
- Correlation analysis
- Distribution plots
- Histograms
- Boxplots
- Countplots
- Pairwise feature analysis

### Feature Engineering

Created two additional features:

- Total Score
- Average Score

---

## ⚙️ Data Preprocessing

Applied:

- One Hot Encoding for categorical features
- Standard Scaling for numerical features
- Column Transformer pipeline

Libraries used:

- pandas
- numpy
- scikit-learn

---

## 🤖 Machine Learning Models

The following regression algorithms were trained:

- Linear Regression
- Lasso Regression
- Ridge Regression
- K-Neighbors Regressor
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor
- CatBoost Regressor
- AdaBoost Regressor

---

## 📈 Model Evaluation

Evaluation Metrics:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

The models were compared based on their predictive performance.

---

## 📉 Visualization

The project includes:

- Histograms
- Countplots
- Correlation Heatmap
- Boxplots
- Actual vs Predicted Scatter Plot

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost
- CatBoost
- Jupyter Notebook

---

## 🚀 How to Run

1. Clone the repository

```bash
git clone https://github.com/Shrirang45/ML-project.git
```

2. Navigate to project

```bash
cd ML-project
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Launch Jupyter Notebook

```bash
jupyter notebook
```

5. Run:

- `1. EDA and Feature Engineering.ipynb`
- `2. Model Training.ipynb`

---

## 📌 Future Improvements

- Build an end-to-end ML pipeline
- Add model serialization using Pickle
- Create a prediction web app using Flask
- Deploy the project on Render or AWS

---

## 👨‍💻 Author

**Shrirang Ambure**

GitHub: https://github.com/Shrirang45
