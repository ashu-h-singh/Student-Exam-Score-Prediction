🎓 Student Exam Score Prediction
Predicting student exam scores using machine learning based on study habits, attendance, and performance indicators using Streamlit and Python.

📌 Project Overview
The Student Exam Score Prediction project aims to build a machine learning system that can forecast students' final exam scores by analyzing academic and behavioral data. Leveraging Python and Streamlit, this project provides an interactive web interface where educators or students can input relevant parameters and get real-time score predictions.

This tool helps in early identification of struggling students, supports personalized learning paths, and promotes data-driven decision-making in education.

🎯 Objectives
Develop a regression-based ML model to predict student exam scores.

Identify key factors impacting student performance.

Provide an intuitive web-based interface using Streamlit.

Assist educators in early intervention and progress tracking.

🧠 Key Features
Interactive UI to enter student data and get real-time score predictions.

Machine learning models trained on real-world datasets.

Data preprocessing, feature engineering, and model evaluation pipeline.

Visual insights (charts, correlation heatmaps, feature importance).

Easy deployment via Streamlit.

Attributes:
Demographics: age, sex, address, famsize, Pstatus

Academics: studytime, failures, absences, G1, G2, G3

Lifestyle: internet, activities, health, traveltime, etc.

Final Score: G3 (target variable)

🛠️ Tech Stack
👨‍💻 Development Environment:
Visual Studio Code (VS Code)
OS: Windows/Linux/Mac

💻 Programming Language:
Python 3.8+

📦 Libraries:
pandas, numpy – Data manipulation

matplotlib, seaborn, plotly – Visualization

scikit-learn – ML models and preprocessing

xgboost – Advanced boosting models

streamlit – Web app interface

joblib – Model serialization

🔁 Workflow
Data Loading & Preprocessing

Load UCI dataset into DataFrame.

Handle missing values and encode categorical variables.

Feature scaling and train-test split.

Exploratory Data Analysis (EDA)

Visualizations (distribution plots, correlation matrix, box plots).

Feature importance using tree-based models.

Model Development

Train multiple regression models:

Linear Regression

Random Forest Regressor

XGBoost Regressor

Evaluate using:

R² Score

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

Model Selection & Saving

Save the best-performing model using joblib.

Streamlit App Development

Create UI for entering student details.

Load the trained model and display predicted exam score.

Add interactive visuals and insights.

🖥️ Streamlit Interface Features
Sidebar inputs for user details (age, studytime, failures, etc.)

Predict button with instant result output.

Graphs for feature impact and score trends.

Educational tips and interpretations (optional add-on).

📊 Example Results
Model	R² Score	RMSE	MAE
Linear Regression	0.84	2.5	1.8
Random Forest Regr.	0.91	1.8	1.2
XGBoost Regr.	0.93	1.6	1.1

(Performance will vary based on tuning and feature engineering)
