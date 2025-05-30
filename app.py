import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("gld_model.pkl")

# Streamlit UI
st.title("💰 Gold Price Prediction App")
st.write("Enter the market values below to predict the GLD price.")

# Input fields
spx = st.number_input("S&P 500 Index (SPX)", value=1400.5)
uso = st.number_input("United States Oil Fund (USO)", value=38.4)
slv = st.number_input("Silver ETF (SLV)", value=28.1)
eur_usd = st.number_input("EUR/USD", value=1.25)

# Predict button
if st.button("Predict GLD Price"):
    features = np.array([[spx, uso, slv, eur_usd]])
    prediction = model.predict(features)
    st.success(f"📈 Predicted GLD Price: ${round(prediction[0], 2)}")



    