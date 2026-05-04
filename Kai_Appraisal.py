import streamlit as st
import pandas as pd
import pickle
import os

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="AutoAppraise - Valuation", page_icon="🏎️")
st.title("Discover Your Car's True Value")
st.write("Enter your vehicle details below to get an instant, AI-driven market appraisal.")
st.write("---")

# --- 2. LOAD THE MODEL ---
# We load the model FIRST so we can use its memory to populate the dropdown menus!
@st.cache_resource # This tells Streamlit to only load the heavy model once
def load_model():
    # Adjust this path if your pkl file is in a different folder relative to this script
    model_path = os.path.join(os.path.dirname(__file__), 'Jovin_Folder', 'model.pkl')
    try:
        with open(model_path, 'rb') as f:
            model, trained_columns = pickle.load(f)
        return model, trained_columns
    except FileNotFoundError:
        # Fallback if the path above fails
        try:
             with open('Jovin_Folder/model.pkl', 'rb') as f:
                model, trained_columns = pickle.load(f)
             return model, trained_columns
        except FileNotFoundError:
            return None, None

model, trained_columns = load_model()

if model is None:
    st.error("⚠️ Could not locate the Machine Learning model (`model.pkl`). Please ensure it is in the correct folder.")
    st.stop() # Stop running the page if the model is missing

# --- 3. DYNAMIC DROPDOWNS (Clean approach) ---
# Instead of hardcoding every brand and model with if/elif, we use dictionaries.
car_database = {
    'Audi': ['A4', 'A6', 'A8', 'Q7'],
    'BMW': ['3 Series', '5 Series', '7 Series', 'X5'],
    'Chevrolet': ['Spark'],
    'Dacia': ['Sandero'],
    'Fiat': ['500'],
    'Ford': ['F-150', 'Focus', 'Mustang'],
    'Honda': ['Accord', 'Civic'],
    'Hyundai': ['Elantra', 'Tucson', 'i10'],
    'Kia': ['Picanto', 'Sportage'],
    'Mazda': ['CX-5', 'MX-5 Miata', 'Mazda3'],
    'Mercedes-Benz': ['C-Class', 'E-Class', 'GLE', 'S-Class'],
    'Peugeot': ['208'],
    'Porsche': ['718 Cayman', '911 Carrera', 'Panamera'],
    'Renault': ['Clio'],
    'Tesla': ['Model 3', 'Model S', 'Model Y'],
    'Toyota': ['Camry', 'Corolla', 'RAV4', 'Supra', 'Yaris'],
    'Volkswagen': ['Golf', 'Tiguan'],
}

# --- 4. USER INPUT SECTION ---
# Using columns makes the form look much more professional
col1, col2 = st.columns(2)

with col1:
    object_brand = st.selectbox("Brand", list(car_database.keys()))
    
    # The models available change based on the brand selected!
    object_model = st.selectbox("Model", car_database[object_brand])
    
    object_year = st.number_input("Year", min_value=1990, max_value=2026, value=2020)

with col2:
    object_mileage = st.number_input("Mileage (in km)", min_value=0, max_value=500000, value=50000, step=5000)
    
    # We need to ask for a few more things because the model was trained on them
    object_condition = st.selectbox("Condition", ["Used", "Excellent", "Fair"])
    object_fuel = st.selectbox("Fuel Type", ["Gasoline", "Diesel", "Hybrid", "Electric"])
    st.subheader("Technical Specifications & History")

col3, col4 = st.columns(2)

with col3:
    object_engine = st.slider("Engine Size (L)", min_value=0.0, max_value=6.0, value=2.0, step=0.1)
    object_hp = st.number_input("Horsepower", min_value=65, max_value=905, value=240)
    object_torque = st.number_input("Torque (Nm)", min_value=16, max_value=850, value=300)
    object_transmission = st.selectbox("Transmission", ["Automatic", "Manual"])

with col4:
    object_drive = st.selectbox("Drive Type", ["AWD", "FWD", "RWD"])
    object_body = st.selectbox("Body Type", ["Convertible", "Coupe", "Hatchback", "Pickup", "SUV", "Sedan"])
    object_accident = st.selectbox("Accident History", ["No", "Yes"])

st.write("---")

# --- 5. PREDICTION LOGIC ---
if st.button("Calculate Value 📊", type="primary", use_container_width=True):
    
    # Show a spinner while the model "thinks"
    with st.spinner("Analyzing market data..."):
        
        # 1. Create a DataFrame with the user's input
        user_input = pd.DataFrame([{
            'Year': object_year,
            'CarAge': 2026 - object_year, 
            'Mileage(km)': object_mileage,
            'Brand': object_brand,
            'Model': object_model,
            'Condition': object_condition, 
            'FuelType': object_fuel, 
            'EngineSize(L)': object_engine,     
            'Horsepower': object_hp,            
            'Torque': object_torque,            
            'Transmission': object_transmission,
            'DriveType': object_drive,          
            'BodyType': object_body,            
            'AccidentHistory': object_accident
        }])

        # 2. Apply One-Hot Encoding
        user_encoded = pd.get_dummies(user_input)

        # 3. Align columns to match the trained model
        user_encoded = user_encoded.reindex(columns=trained_columns, fill_value=0)

        # 4. Make the Prediction
        prediction = model.predict(user_encoded)
        predicted_price = prediction[0]
        
    # --- 6. DISPLAY RESULTS ---
    st.balloons() # Fun Streamlit animation
    
    st.success("Valuation Complete!")
    
    # Display the price in a large, nice format
    st.metric(label="Estimated Fair Market Value", value=f"${predicted_price:,.2f}")
    
    st.caption("Disclaimer: This is an AI-generated estimate based on historical data. Actual market prices may vary.")