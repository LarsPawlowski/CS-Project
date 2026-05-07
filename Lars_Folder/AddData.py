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

# Load brands and types from the dataset
df = pd.read_csv("car_price_dataset.csv")
#Brand selectbox
brands = sorted(df["Brand"].dropna().astype(str).unique())
object_brand = st.selectbox("Brand", brands)
# Clean columns
df["Brand"] = df["Brand"].astype(str).str.strip()
df["Model"] = df["Model"].astype(str).str.strip()
# Match car types to brands
filtered_df = df[df["Brand"] == object_brand]
models = sorted(filtered_df["Model"].dropna().unique())
# Model selectbox
object_model = st.selectbox("Model", models, key="model_select")
# Remaining inputs
object_year = st.number_input("Year", min_value=1990, max_value=2026, value=2023)
object_mileage = st.number_input("Mileage (km)", min_value=0, value=50000)
object_price = st.number_input("Price ($)", min_value=0, value=20000)
conditions = ["None"] + sorted(df["Condition"].dropna().astype(str).unique().tolist())
object_condition = st.selectbox("Condition", conditions)

engine_sizes = ["None"] + sorted(df["EngineSize(L)"].dropna().astype(str).unique().tolist())
object_engine = st.selectbox("Engine Size (L)", engine_sizes)

fuel_types = ["None"] + sorted(df["FuelType"].dropna().astype(str).unique().tolist())
object_fuel = st.selectbox("Fuel Type", fuel_types)

horsepower_values = ["None"] + sorted(df["Horsepower"].dropna().astype(str).unique().tolist())
object_horsepower = st.selectbox("Horsepower", horsepower_values)

torque_values = ["None"] + sorted(df["Torque"].dropna().astype(str).unique().tolist())
object_torque = st.selectbox("Torque", torque_values)

transmissions = ["None"] + sorted(df["Transmission"].dropna().astype(str).unique().tolist())
object_transmission = st.selectbox("Transmission", transmissions)

drive_types = ["None"] + sorted(df["DriveType"].dropna().astype(str).unique().tolist())
object_drive = st.selectbox("Drive Type", drive_types)

body_types = ["None"] + sorted(df["BodyType"].dropna().astype(str).unique().tolist())
object_body = st.selectbox("Body Type", body_types)

doors_values = ["None"] + sorted(df["Doors"].dropna().astype(str).unique().tolist())
object_doors = st.selectbox("Doors", doors_values)

seats_values = ["None"] + sorted(df["Seats"].dropna().astype(str).unique().tolist())
object_seats = st.selectbox("Seats", seats_values)

colors = ["None"] + sorted(df["Color"].dropna().astype(str).unique().tolist())
object_color = st.selectbox("Color", colors)

interiors = ["None"] + sorted(df["Interior"].dropna().astype(str).unique().tolist())
object_interior = st.selectbox("Interior", interiors)

options_values = ["None"] + sorted(df["Options"].dropna().astype(str).unique().tolist())
object_options = st.selectbox("Options", options_values)

cities = ["None"] + sorted(df["City"].dropna().astype(str).unique().tolist())
object_city = st.selectbox("City", cities)

accident_values = ["None"] + sorted(df["AccidentHistory"].dropna().astype(str).unique().tolist())
object_accident = st.selectbox("Accident History", accident_values)

insurance_values = ["None"] + sorted(df["Insurance"].dropna().astype(str).unique().tolist())
object_insurance = st.selectbox("Insurance", insurance_values)

registration_values = ["None"] + sorted(df["RegistrationStatus"].dropna().astype(str).unique().tolist())
object_registration = st.selectbox("Registration Status", registration_values)

fuel_efficiency_values = ["None"] + sorted(df["FuelEfficiency(L/100km)"].dropna().astype(str).unique().tolist())
object_fuel_efficiency = st.selectbox("Fuel Efficiency (L/100km)", fuel_efficiency_values)

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
            "CarAge": 2026 - object_year,

            "Condition": None if object_condition == "None" else object_condition,

            "Mileage(km)": object_mileage,

            "EngineSize(L)": None if object_engine == "None" else float(object_engine),

            "FuelType": None if object_fuel == "None" else object_fuel,

            "Horsepower": None if object_horsepower == "None" else int(float(object_horsepower)),
            "Torque": None if object_torque == "None" else int(float(object_torque)),
            "Transmission": None if object_transmission == "None" else object_transmission,

            "DriveType": None if object_drive == "None" else object_drive,

            "BodyType": None if object_body == "None" else object_body,

            "Doors": None if object_doors == "None" else int(float(object_doors)),

            "Seats": None if object_seats == "None" else int(float(object_seats)),

            "Color": None if object_color == "None" else object_color,

            "Interior": None if object_interior == "None" else object_interior,

            "Options": None if object_options == "None" else object_options,

            "City": None if object_city == "None" else object_city,

            "AccidentHistory": None if object_accident == "None" else object_accident,

            "Insurance": None if object_insurance == "None" else object_insurance,

            "RegistrationStatus": None if object_registration == "None" else object_registration,

            "FuelEfficiency(L/100km)": None if object_fuel_efficiency == "None" else object_fuel_efficiency,

            "PricePerKm": object_price / object_mileage if object_mileage > 0 else 0,

            "Price($)": object_price
}

        new_df = pd.DataFrame([new_data])

        new_df.to_csv("car_price_dataset.csv", mode="a", header=False, index=False)

        st.success("Thank you! Your data has been added to the dataset.")
# Back to Homepage Button
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("Back to Homepage"):
        st.write("Redirecting to homepage...")