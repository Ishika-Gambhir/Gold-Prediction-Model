import streamlit as st
import pandas as pd
import joblib
import os
import sklearn

# === Load your trained model ===
MODEL_FILENAME = 'rf_model.pkl'

# Check if model file exists
if os.path.exists(MODEL_FILENAME):
    model = joblib.load(MODEL_FILENAME)
else:
    st.error(f"Model file '{MODEL_FILENAME}' not found.")
    st.stop()

# === Streamlit UI ===
st.set_page_config(page_title="Gold Price Prediction", layout="centered")
st.title("💰 Gold Price Prediction App")
st.markdown("Enter the market indicator values below to predict the price of gold.")

# Input form
with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        spx = st.number_input("📈 SPX (S&P 500 Index)", min_value=0.0, step=0.1, value=4000.0)
        slv = st.number_input("🥈 SLV (Silver Trust)", min_value=0.0, step=0.1, value=20.0)
    with col2:
        uso = st.number_input("🛢️ USO (Oil Fund)", min_value=0.0, step=0.1, value=60.0)
        eur_usd = st.number_input("💱 EUR/USD", min_value=0.0, step=0.001, value=1.1, format="%.3f")

    submit = st.form_submit_button("Predict Gold Price")

# Handle prediction
if submit:
    try:
        input_df = pd.DataFrame([[spx, uso, slv, eur_usd]], columns=["SPX", "USO", "SLV", "EUR/USD"])
        prediction = model.predict(input_df)[0]
        st.success(f"📊 Predicted Gold Price: **${prediction:.2f}**")
    except Exception as e:
        st.error(f"⚠️ Error making prediction: {e}")
