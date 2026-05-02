#CODE TO ADD DATA TO DATASETS
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# Page for Adding Data To the Datasets (if you sold a car you can add it here)
# Tab Title
st.set_page_config(page_title="AutoAppraise - Sold Cars", page_icon="🏎️")
# Title & Intro
st.title("AutoAppraise")
st.subheader("Inform us about sold cars to help us improve our appraise model!")

# Load brands and types from carvana.csv
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "carvana.csv")

df = pd.read_csv(file_path)
brands = sorted(df["Brand"].dropna().astype(str).unique())
#brand selectbox
object_brand = st.selectbox("Brand", brands)

# Clean columns once
df["Brand"] = df["Brand"].astype(str).str.strip()
df["Type"] = df["Type"].astype(str).str.strip()

# Match car types to brand
filtered_df = df[df["Brand"] == object_brand]

types = sorted(filtered_df["Type"].dropna().unique())
#type selectbox
object_type = st.selectbox("Type", types, key="type_select")
#remaining inputs
object_year = st.number_input("Year", min_value=1990, max_value=2026, value=2023)
object_miles = st.number_input("Miles", min_value=0, value=50000)
object_price = st.number_input("Price Sold", min_value=0, value=20000)
#Image Upload section for veriifcation of the data, Coded by VSCODE AI
object_image = st.file_uploader("Upload Documentation for Verification of Sale", type=["jpg", "png"])
#Data Submission
if st.button("Submit"):
    if object_image is None:
        st.error("Please upload documentation before submitting.")
    else:
        # -----------------------------
        # ADD THIS BLOCK
        # -----------------------------
        new_data = {
            "Brand": object_brand.strip(),
            "Type": object_type.strip(),
            "Year": object_year,
            "Miles": object_miles,
            "Price": object_price
        }

        new_df = pd.DataFrame([new_data])

        # Append to CSV (without overwriting)
        new_df.to_csv(file_path, mode="a", header=False, index=False)
        # -----------------------------

        st.success("Thank you for your submission! Your data will be reviewed and added to our dataset.")

col1, col2, col3 = st.columns(3)
with col2:
    if st.button("Back to Homepage"):
        st.write("Redirecting to homepage...")