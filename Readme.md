
# 🟡 Gold Price Prediction Model

Welcome to the **Gold Price Prediction Model** repository!  
This project uses machine learning techniques to predict gold prices based on historical market and economic data.

## 📊 Overview

Gold is considered a safe-haven asset, and its price is influenced by various global factors including currency exchange rates, inflation, interest rates, and geopolitical events.  
In this project, we explore a dataset of historical gold prices and build a machine learning model that forecasts future prices with promising accuracy.

## 🚀 Features

- Data preprocessing and feature engineering
- Exploratory Data Analysis (EDA)
- Model training with regression algorithms
- Performance evaluation using metrics like RMSE, R² score
- Prediction visualization

## 🧠 Machine Learning Models Used

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor
- Support Vector Regression (SVR)

## 🛠️ Tech Stack

- Python
- Jupyter Notebook
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn
- XGBoost

## 📁 Project Structure

```
gold-prediction-model/
│
├── data/                     # Contains the gold price dataset
├── notebooks/                # Jupyter notebooks with code and analysis
├── models/                   # Saved models (Pickle or joblib format)
├── visuals/                  # Charts and plots generated
├── requirements.txt          # Required Python packages
└── README.md                 # Project documentation
```

## 📈 Dataset

The dataset includes:
- Date-wise gold prices (target variable)
- Features like USD exchange rate, crude oil prices, inflation rate, etc.

> Source: [Kaggle Gold Price Dataset](https://www.kaggle.com/datasets)

## 🧪 How to Use

1. **Clone the repository**

```bash
git clone https://github.com/ishika-gambhir/gold-prediction-model.git
cd gold-prediction-model
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the notebook**

Open the Jupyter Notebook and follow the steps in the `.ipynb` file to explore data, train models, and visualize predictions.

## 📉 Sample Output

![Gold Price Predictions](visuals/predicted_vs_actual.png)

## 📚 Future Improvements

- Incorporate LSTM/Deep Learning models
- Add real-time data fetching via APIs
- Deploy as a web app using Flask/Streamlit

## 👩‍💻 Author

**Ishika Gambhir**  
B.Tech in Electrical Engineering  
[GitHub](https://github.com/ishika-gambhir) | [LinkedIn](https://www.linkedin.com/in/ishika-gambhir)

## 🌟 Show Your Support

If you like this project, feel free to ⭐ the repository and share it with others!
