# EXAMPLE CODE
# Required Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Tab Title
st.set_page_config(page_title="AutoAppraise - Your Cars True Value", page_icon="🏎️")
# Title & Intro
st.title("Welcome to AutoAppraise!")

# Our Mission
if st.button("About Us"):
    st.write("""
Welcome to AutoAppraise, the ultimate tool for car enthusiasts and buyers alike! Our mission is to provide you with accurate and up-to-date information about your car's true value. Whether you're looking to sell, buy, or simply curious about your vehicle's worth, AutoAppraise has got you covered. With our user-friendly interface and powerful algorithms, you can easily get an estimate of your car's value based on its make, model, year, mileage, and condition. Join us on this exciting journey to discover the true value of your car and make informed decisions in the automotive market!
""")


# Enter Car Details (Matches brand to available models)
st.subheader("Discover Your Car's True Value")
brands = ["Mercedes Benz", "BMW", "Porsche", "Volvo", "Lamborghini", "Ferrari", "Audi", "Volkswagen", "Toyota", "Honda"]
object_brand = st.selectbox("Brand", brands)
mercmodels = ["Mercedes A", "Mercedes B", "Mercedes C", "Mercedes D", "Mercedes E", "Mercedes F", "Mercedes G"]
bmwmodels = ["BMW A", "BMW B", "BMW C", "BMW D", "BMW E", "BMW F", "BMW G"]
porschemodels = ["Porsche A", "Porsche B", "Porsche C", "Porsche D", "Porsche E", "Porsche F", "Porsche G"]
volvomodels = ["Volvo A", "Volvo B", "Volvo C", "Volvo D", "Volvo E", "Volvo F", "Volvo G"]
lamborghinimodels = ["Lamborghini A", "Lamborghini B", "Lamborghini C", "Lamborghini D", "Lamborghini E", "Lamborghini F", "Lamborghini G"]
ferrarimodels = ["Ferrari A", "Ferrari B", "Ferrari C", "Ferrari D", "Ferrari E", "Ferrari F", "Ferrari G"]
audimodels = ["Audi A", "Audi B", "Audi C", "Audi D", "Audi E", "Audi F", "Audi G"]
volkswagenmodels = ["Volkswagen A", "Volkswagen B", "Volkswagen C", "Volkswagen D", "Volkswagen E", "Volkswagen F", "Volkswagen G"]
toyotamodels = ["Toyota A", "Toyota B", "Toyota C", "Toyota D", "Toyota E", "Toyota F", "Toyota G"]
hondamodels = ["Honda A", "Honda B", "Honda C", "Honda D", "Honda E", "Honda F", "Honda G"]
if object_brand == "Mercedes Benz":
    models = mercmodels
elif object_brand == "BMW":
    models = bmwmodels
elif object_brand == "Porsche":
    models = porschemodels
elif object_brand == "Volvo":
    models = volvomodels
elif object_brand == "Lamborghini":
    models = lamborghinimodels
elif object_brand == "Ferrari":
    models = ferrarimodels
elif object_brand == "Audi":
    models = audimodels
elif object_brand == "Volkswagen":
    models = volkswagenmodels
elif object_brand == "Toyota":
    models = toyotamodels
elif object_brand == "Honda":
    models = hondamodels
object_model = st.selectbox("Model", models)
object_year = st.number_input("Year", min_value=1990, max_value=2026, value=2023)
object_mileage = st.number_input("Mileage (in km)", min_value=0, value=50000)

# KAIS INPUT