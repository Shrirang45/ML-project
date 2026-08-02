# 🎓 Student Performance Indicator (End-to-End Machine Learning Project)

An End-to-End Machine Learning application that predicts a student's **Mathematics Score** using demographic and academic information. The project demonstrates the complete ML workflow, including data preprocessing, model training, model selection, Flask integration, and cloud deployment.

🌐 **Live Demo:** https://student-performance-indicator-end-to-end-b9rf.onrender.com

---

# 📌 Project Overview

The objective of this project is to predict a student's **Math Score** based on several demographic and academic features.

This project follows a production-style machine learning pipeline and includes:

- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Ingestion
- Data Transformation
- Model Training
- Hyperparameter Tuning
- Prediction Pipeline
- Flask Web Application
- Deployment on Render

---

# 📂 Project Structure

```text
Student Performance Indicator/
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   ├── test.csv
│   └── raw.csv
│
├── notebooks/
│   ├── 1. EDA and Feature Engineering.ipynb
│   ├── 2. Model Training.ipynb
│   └── StudentsPerformance.csv
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   └── predict_pipeline.py
│   │
│   ├── logger.py
│   ├── exception.py
│   └── utils.py
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── app.py
├── requirements.txt
├── setup.py
├── README.md
└── .gitignore
```

---

# 📊 Dataset

The dataset contains information about students including:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score
- Mathematics Score (Target Variable)

---

# 🔍 Exploratory Data Analysis

Performed:

- Dataset inspection
- Missing value analysis
- Duplicate value check
- Data type identification
- Statistical summary
- Correlation analysis
- Distribution plots
- Histograms
- Count plots
- Box plots

### Feature Engineering

Additional features created during analysis:

- Total Score
- Average Score

---

# ⚙️ Machine Learning Pipeline

## 1️⃣ Data Ingestion

- Reads the dataset
- Splits into training and testing datasets
- Saves:
  - raw.csv
  - train.csv
  - test.csv

---

## 2️⃣ Data Transformation

Preprocessing is implemented using Scikit-learn Pipelines.

### Numerical Pipeline

- Missing value imputation
- Standard Scaling

### Categorical Pipeline

- Missing value imputation
- One Hot Encoding

The preprocessing pipeline is saved as:

```
preprocessor.pkl
```

---

## 3️⃣ Model Training

The following regression algorithms were trained and compared:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- AdaBoost Regressor
- KNeighbors Regressor
- XGBoost Regressor
- CatBoost Regressor

Hyperparameter tuning is performed using **GridSearchCV**.

The best-performing model is saved as:

```
model.pkl
```

---

## 4️⃣ Prediction Pipeline

The prediction pipeline:

- Loads the trained model
- Loads the preprocessing object
- Transforms user input
- Predicts Mathematics Score
- Returns prediction to the Flask application

---

# 📈 Model Evaluation

Evaluation Metrics:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

The model with the highest R² score is automatically selected for deployment.

---

# 🌐 Web Application

Users can:

- Select demographic details
- Enter Reading Score
- Enter Writing Score
- Predict Mathematics Score instantly

---

# 🛠️ Technologies Used

### Programming

- Python

### Machine Learning

- Scikit-learn
- XGBoost
- CatBoost

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Web Framework

- Flask

### Deployment

- Gunicorn
- Render

### Version Control

- Git
- GitHub

---

# 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/Shrirang45/ML-project.git
```

### Navigate to the Project

```bash
cd ML-project
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

The application will be available at:

```
http://127.0.0.1:5000
```

---

# 🌍 Deployment

The application is deployed on **Render**.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

---

# 🔄 Application Workflow

```text
User Input
      │
      ▼
Flask Web Form
      │
      ▼
CustomData
      │
      ▼
Pandas DataFrame
      │
      ▼
Preprocessing Pipeline
      │
      ▼
Best Trained Model
      │
      ▼
Predicted Mathematics Score
      │
      ▼
Display Result
```

---

# ✨ Key Features

- End-to-End Machine Learning Pipeline
- Modular Project Structure
- Logging and Custom Exception Handling
- Data Preprocessing Pipeline
- Hyperparameter Tuning
- Model Serialization
- Flask Integration
- Live Deployment on Render

---

# 📌 Future Improvements

- Modern responsive UI
- Docker containerization
- CI/CD pipeline
- Model monitoring
- Cloud model storage
- REST API using FastAPI

---

# 👨‍💻 Author

**Shrirang Ambure**

🎓 B.Tech – Artificial Intelligence & Data Science

GitHub: https://github.com/Shrirang45

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.
