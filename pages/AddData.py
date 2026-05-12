# Page for Adding Data To the Datasets (if you sold a car you can add it here)
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Tab Title
st.set_page_config(page_title="AutoAppraise - Sold Cars", page_icon="🏎️")

# Title & Intro
st.title("AutoAppraise")
st.subheader("Inform us about sold cars to help us improve our appraise model!")

# Load dataset
df = pd.read_csv("ML/car_price_dataset.csv")

# Brand selectbox
brands = sorted(df["Brand"].dropna().astype(str).unique())
object_brand = st.selectbox("Brand", brands)

# Clean columns
df["Brand"] = df["Brand"].astype(str).str.strip()
df["Model"] = df["Model"].astype(str).str.strip()

# Match car models to brands
filtered_df = df[df["Brand"] == object_brand]
models = sorted(filtered_df["Model"].dropna().unique())

# Model selectbox
object_model = st.selectbox("Model", models, key="model_select")

# Main inputs
object_year = st.number_input("Year", min_value=1990, max_value=2026, value=2023)
object_mileage = st.number_input("Mileage (km)", min_value=0, value=50000)
object_price = st.number_input("Price ($)", min_value=0, value=20000)

# Condition
conditions = ["None"] + sorted(df["Condition"].dropna().astype(str).unique().tolist())
object_condition = st.selectbox("Condition", conditions)

# Engine Size Slider
engine_min = float(df["EngineSize(L)"].dropna().min())
engine_max = float(df["EngineSize(L)"].dropna().max())
object_engine = st.slider(
    "Engine Size (L)",
    min_value=engine_min,
    max_value=engine_max,
    value=engine_min,
    step=0.1
)

# Fuel Type
fuel_types = ["None"] + sorted(df["FuelType"].dropna().astype(str).unique().tolist())
object_fuel = st.selectbox("Fuel Type", fuel_types)

# Horsepower Slider
horsepower_min = int(df["Horsepower"].dropna().min())
horsepower_max = int(df["Horsepower"].dropna().max())
object_horsepower = st.slider(
    "Horsepower",
    min_value=horsepower_min,
    max_value=horsepower_max,
    value=horsepower_min
)

# Torque Slider
torque_min = int(df["Torque"].dropna().min())
torque_max = int(df["Torque"].dropna().max())
object_torque = st.slider(
    "Torque",
    min_value=torque_min,
    max_value=torque_max,
    value=torque_min
)
# Transmission
transmissions = ["None"] + sorted(df["Transmission"].dropna().astype(str).unique().tolist())
object_transmission = st.selectbox("Transmission", transmissions)
# Drive Type
drive_types = ["None"] + sorted(df["DriveType"].dropna().astype(str).unique().tolist())
object_drive = st.selectbox("Drive Type", drive_types)
# Seats Slider
seats_min = int(df["Seats"].dropna().min())
seats_max = int(df["Seats"].dropna().max())
object_seats = st.slider(
    "Seats",
    min_value=seats_min,
    max_value=seats_max,
    value=seats_min
)

# Color
colors = ["None"] + sorted(df["Color"].dropna().astype(str).unique().tolist())
object_color = st.selectbox("Color", colors)
# Options
options_values = ["None"] + sorted(df["Options"].dropna().astype(str).unique().tolist())
object_options = st.selectbox("Options", options_values)
# Accident History
accident_values = ["None"] + sorted(df["AccidentHistory"].dropna().astype(str).unique().tolist())
object_accident = st.selectbox("Accident History", accident_values)
# Insurance
insurance_values = ["None"] + sorted(df["Insurance"].dropna().astype(str).unique().tolist())
object_insurance = st.selectbox("Insurance", insurance_values)
# Registration
registration_values = ["None"] + sorted(df["RegistrationStatus"].dropna().astype(str).unique().tolist())
object_registration = st.selectbox("Registration Status", registration_values)
# Fuel Efficiency Slider
fuel_min = float(df["FuelEfficiency(L/100km)"].dropna().min())
fuel_max = float(df["FuelEfficiency(L/100km)"].dropna().max())
object_fuel_efficiency = st.slider(
    "Fuel Efficiency (L/100km)",
    min_value=fuel_min,
    max_value=fuel_max,
    value=fuel_min,
    step=0.1
)

# Image verification upload (non functional)
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
            "CarAge": datetime.now().year - object_year,
            "Condition": None if object_condition == "None" else object_condition,
            "Mileage(km)": object_mileage,
            "EngineSize(L)": object_engine,
            "FuelType": None if object_fuel == "None" else object_fuel,
            "Horsepower": object_horsepower,
            "Torque": object_torque,
            "Transmission": None if object_transmission == "None" else object_transmission,
            "DriveType": None if object_drive == "None" else object_drive,
            "Seats": object_seats,
            "Color": None if object_color == "None" else object_color,
            "Options": None if object_options == "None" else object_options,
            "AccidentHistory": None if object_accident == "None" else object_accident,
            "Insurance": None if object_insurance == "None" else object_insurance,
            "RegistrationStatus": None if object_registration == "None" else object_registration,
            "FuelEfficiency(L/100km)": object_fuel_efficiency,
            "Price($)": object_price
        }
        new_df = pd.DataFrame([new_data])
        new_df.to_csv("ML/car_price_dataset.csv", mode="a", header=False, index=False)
        st.success("Thank you! Your data has been added to the dataset.")
# Back to Homepage Button
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("Back to Homepage"):
        st.write("Redirecting to homepage...")
        st.switch_page("MainPage.py")
        
