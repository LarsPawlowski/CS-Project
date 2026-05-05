# Page for Adding Data To the Datasets (if you sold a car you can add it here)
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Tab Title
st.set_page_config(page_title="AutoAppraise - Sold Cars", page_icon="🏎️")

# Title & Intro
st.title("AutoAppraise")
st.subheader("Inform us about sold cars to help us improve our appraise model!")

# Load dataset
df = pd.read_csv("car_price_dataset.csv")

# Brand select
brands = sorted(df["Brand"].dropna().astype(str).unique())
object_brand = st.selectbox("Brand", brands)

# Clean columns
df["Brand"] = df["Brand"].astype(str).str.strip()
df["Model"] = df["Model"].astype(str).str.strip()

# Match models to brand
filtered_df = df[df["Brand"] == object_brand]
models = sorted(filtered_df["Model"].dropna().unique())

# Model selectbox
object_model = st.selectbox("Model", models, key="model_select")

# Remaining inputs
object_year = st.number_input("Year", min_value=1990, max_value=2026, value=2023)
object_mileage = st.number_input("Mileage (km)", min_value=0, value=50000)
object_price = st.number_input("Price ($)", min_value=0, value=20000)

# Image upload
object_image = st.file_uploader(
    "Upload Documentation for Verification of Sale", 
    type=["jpg", "png"]
)

# Data Submission
if st.button("Submit"):
    if object_image is None:
        st.error("Please upload documentation before submitting.")
    else:
        new_data = {
            "Brand": object_brand.strip(),
            "Model": object_model.strip(),
            "Year": object_year,
            "CarAge": 2026 - object_year,  # simple calculation
            "Condition": "Used",
            "Mileage(km)": object_mileage,
            "EngineSize(L)": None,
            "FuelType": None,
            "Horsepower": None,
            "Torque": None,
            "Transmission": None,
            "DriveType": None,
            "BodyType": None,
            "Doors": None,
            "Seats": None,
            "Color": None,
            "Interior": None,
            "Options": None,
            "City": None,
            "AccidentHistory": None,
            "Insurance": None,
            "RegistrationStatus": None,
            "FuelEfficiency(L/100km)": None,
            "PricePerKm": object_price / object_mileage if object_mileage > 0 else 0,
            "Price($)": object_price
        }

        new_df = pd.DataFrame([new_data])

        # Append to CSV
        new_df.to_csv("car_price_dataset.csv", mode="a", header=False, index=False)

        st.success("Thank you! Your data has been added to the dataset.")

# Navigation
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("Back to Homepage"):
        st.write("Redirecting to homepage...")