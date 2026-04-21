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
st.write("""
Welcome to AutoAppraise, the ultimate tool for car enthusiasts and buyers alike! Our mission is to provide you with accurate and up-to-date information about your car's true value. Whether you're looking to sell, buy, or simply curious about your vehicle's worth, AutoAppraise has got you covered. With our user-friendly interface and powerful algorithms, you can easily get an estimate of your car's value based on its make, model, year, mileage, and condition. Join us on this exciting journey to discover the true value of your car and make informed decisions in the automotive market!
""")
# Our Mission
if st.button("About Us"):
    st.write("This is a Streamlit tutorial for FCS bachelor students!")
    st.write("""
Welcome to AutoAppraise, the ultimate tool for car enthusiasts and buyers alike! Our mission is to provide you with accurate and up-to-date information about your car's true value. Whether you're looking to sell, buy, or simply curious about your vehicle's worth, AutoAppraise has got you covered. With our user-friendly interface and powerful algorithms, you can easily get an estimate of your car's value based on its make, model, year, mileage, and condition. Join us on this exciting journey to discover the true value of your car and make informed decisions in the automotive market!
""")


# Text Input
st.subheader("Discover Your Car's True Value")
name = st.text_input("Enter your name", placeholder="Your name here...")
if name != "":
    st.write(f"Hello, {name}! Welcome to FCS!")