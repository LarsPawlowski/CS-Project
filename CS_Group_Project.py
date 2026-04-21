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
Welcome to the interactive Streamlit tutorial tailored for FCS bachelor students! 
Here's a introductory showcase of what you can achieve using Streamlit with very little code.
""")

# Text Input
st.subheader("Text Input")
name = st.text_input("Enter your name", placeholder="Your name here...")
if name != "":
    st.write(f"Hello, {name}! Welcome to FCS!")