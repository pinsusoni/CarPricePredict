import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("car_price_model.pkl")

st.title("🚗 Car Price Prediction App")

# Input fields
name = st.text_input("Car Name (e.g. Swift, Alto, City)")
company = st.text_input("Company (e.g. Maruti, Hyundai, Honda)")
year = st.number_input("Year of Purchase", min_value=1990, max_value=2025, step=1)
kms_driven = st.number_input("Kilometers Driven", min_value=0, step=1000)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])

# Predict button
if st.button("Predict Price"):
    # Convert inputs into DataFrame
    input_df = pd.DataFrame({
        "name": [name],
        "company": [company],
        "year": [year],
        "kms_driven": [kms_driven],
        "fuel_type": [fuel_type]
    })

    # Predict using model
    prediction = model.predict(input_df)[0]

    st.success(f"💰 Estimated Car Price: ₹ {int(prediction):,}")
