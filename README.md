# 💼 Salary Prediction Web App using Linear Regression

This project is a **machine learning web application** that predicts a person's salary based on input factors like:

- Age  
- Gender  
- Education Level  
- Job Title  
- Years of Experience  

It uses a **Linear Regression model** trained on a dataset with over 300 records of real-world job and salary information.

---

## 🚀 Features

- 🔢 Predict salary instantly from user input  
- 📈 Visualize model accuracy using R² score  
- 📊 Compare actual vs predicted salary with a scatter plot  
- 🎨 Stylish and animated frontend interface  
- 🧠 Built using Python, Flask, and Scikit-Learn  

---

## 🔍 Dataset

- **Source**: Synthetic dataset modeled after real job market data  
- **Size**: ~300+ entries  
- **Columns**: `Age`, `Gender`, `Education Level`, `Job Title`, `Years of Experience`, `Salary`

---

## 📷 Sample Prediction Plot

![Actual vs Predicted Salary](./static/salary_plot.png)

> Most points lie close to the red line (perfect prediction), indicating a **high accuracy model**.

---

## 📈 Model Used

- ✅ **Linear Regression** from `sklearn.linear_model`
- 🎯 Achieved **R² score ≈ 0.94**, indicating a good fit  
- Handled categorical features using **One-Hot Encoding**

---

## 🛠️ Tech Stack

- **Frontend**: HTML + CSS (with animations)
- **Backend**: Python + Flask
- **ML Model**: Scikit-learn Linear Regression
- **Visualization**: Matplotlib

---

## 🔮 Future Improvements

- 📤 Upload resume and extract features using NLP for salary prediction  
- 📍 Recommend jobs based on location using Google Jobs API  
- 📚 Improve model using more complex algorithms (Random Forest, XGBoost)  
- ☁️ Deploy on cloud (e.g., Render, Heroku, or AWS)

---

## 💡 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/SyedAashiqAhmed/salary-predictor
   cd salary-predictor
