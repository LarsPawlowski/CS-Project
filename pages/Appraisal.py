import streamlit as st
import pandas as pd
import pickle
import os
from datetime import datetime
 
# Page config. 
st.set_page_config(page_title="AutoAppraise - Valuation", page_icon="🏎️", layout="wide")
 
# constant factors for the website 
CURRENCY = "$"  # Change to "CHF", "£", "€", etc. for non-US markets
CURRENT_YEAR = datetime.now().year
 
# Loading the ML model 
@st.cache_resource
def load_model():
    """Load the pre-trained machine learning model"""
    model_path = os.path.join(os.path.dirname(__file__), 'ML', 'model.pkl')
    try:
        with open(model_path, 'rb') as f:
            model, trained_columns = pickle.load(f)
        return model, trained_columns
    except FileNotFoundError:
        # Fallback path
        try:
            with open('ML/model.pkl', 'rb') as f:
                model, trained_columns = pickle.load(f)
            return model, trained_columns
        except FileNotFoundError:
            return None, None
 
model, trained_columns = load_model()
 
if model is None:
    st.error("⚠️ Could not locate the Machine Learning model (`model.pkl`). Please ensure it is in the correct folder.")
    st.stop()
 
# Car database which will be used to obtain the results 
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
 
# --- CUSTOM CSS STYLING --- AI Costum Styling
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2.5rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .main-title {
        color: white;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    .main-subtitle {
        color: #f0f0f0;
        font-size: 1.3rem;
        font-weight: 400;
        margin-bottom: 0.5rem;
    }
    .main-description {
        color: #e8e8e8;
        font-size: 1.05rem;
        line-height: 1.6;
        margin-top: 1rem;
    }
    .feature-badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.2);
        padding: 0.4rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        font-size: 0.9rem;
        color: white;
        backdrop-filter: blur(10px);
    }
    </style>
""", unsafe_allow_html=True)
 
# Appraisal page header 
st.markdown("""
    <div class="main-header">
        <div class="main-title">🏎️ AutoAppraise</div>
        <div class="main-subtitle">Discover Your Car's True Value</div>
        <div class="main-description">
            Welcome to AutoAppraise, your intelligent automotive valuation partner powered by advanced machine learning. 
            Our sophisticated ML model analyzes multiple data points including vehicle specifications, market trends, 
            and historical pricing data to provide you with an accurate, real-time market appraisal. Whether you're 
            looking to sell, trade-in, or simply curious about your vehicle's worth, our platform delivers instant, 
            data-driven insights that help you make informed decisions with confidence.
        </div>
        <div style="margin-top: 1.5rem;">
            <span class="feature-badge">⚡ Instant Results</span>
            <span class="feature-badge">🔒 Secure</span>
            <span class="feature-badge">🤖 AI-Powered</span>
            <span class="feature-badge">📊 Data-Driven</span>
        </div>
    </div>
 """, unsafe_allow_html=True)
 
# Disclaimer for users 
st.info("""
    **ℹ️ Beta Version Notice**  
    This valuation tool is currently in development. Our AI model supports a **limited selection of popular car brands and models**. 
    For the most accurate results, please ensure your vehicle matches one of the available options in the dropdowns below.
    Valuations are estimates based on historical data and may not reflect current market conditions in all regions.
""")
 
# Show supported brands
with st.expander("📋 View Supported Brands & Models"):
    st.write("**Currently supported brands:**")
    brands_list = list(car_database.keys())
    cols = st.columns(3)
    for idx, brand in enumerate(brands_list):
        col_idx = idx % 3
        with cols[col_idx]:
            st.write(f"✓ **{brand}**")
            for model_name in car_database[brand]:
                st.caption(f"  • {model_name}")
    st.caption(f"**Total: {len(brands_list)} brands, {sum(len(models) for models in car_database.values())} models**")
 
st.divider()
 
# input form 
st.subheader("📋 Vehicle Information")
 
col1, col2 = st.columns(2)
 
with col1:
    object_brand = st.selectbox("Brand", list(car_database.keys()))
    object_model = st.selectbox("Model", car_database[object_brand])
    object_year = st.number_input("Year", min_value=1990, max_value=CURRENT_YEAR, value=2020)
    object_mileage = st.number_input("Mileage (in km)", min_value=0, max_value=500000, value=50000, step=5000)
 
with col2:
    object_condition = "Used"  # Set to default
    object_fuel = st.selectbox("Fuel Type", ["Gasoline", "Diesel", "Hybrid", "Electric"])
    object_transmission = st.selectbox("Transmission", ["Automatic", "Manual"])
    object_accident = st.selectbox("Accident History", ["No", "Yes"])
 
st.subheader("🔧 Technical Specifications")
 
col3, col4 = st.columns(2)
 
with col3:
    object_engine = st.slider("Engine Size (L)", min_value=0.66, max_value=6.0, value=2.0, step=0.1)
    object_hp = st.number_input("Horsepower", min_value=65, max_value=905, value=240)
 
with col4:
    object_torque = st.number_input("Torque (Nm)", min_value=16, max_value=850, value=300)
    object_drive = st.selectbox("Drive Type", ["AWD", "FWD", "RWD"])
 
object_body = st.selectbox("Body Type", ["Sedan", "SUV", "Hatchback", "Coupe", "Convertible", "Pickup"])
 
st.divider()
 
# predictor button for car value 
if st.button("Calculate Value 📊", type="primary", use_container_width=True):
    
    with st.spinner("🔍 Analyzing market data and computing valuation..."):
        
        # Prepare input data
        user_input = pd.DataFrame([{
            'Year': object_year,
            'CarAge': CURRENT_YEAR - object_year, 
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
 
        # Apply One-Hot Encoding
        user_encoded = pd.get_dummies(user_input)
 
        # Align columns to match trained model
        user_encoded = user_encoded.reindex(columns=trained_columns, fill_value=0)
 
        # Make Prediction
        prediction = model.predict(user_encoded)
        predicted_price = prediction[0]
        
        # Calculate range (±10% for trade-in and retail)
        trade_in_value = int(predicted_price * 0.90)
        retail_value = int(predicted_price * 1.10)
        
    # result display 
    st.balloons()
    
    st.write("")  # Spacing
    
    # Vehicle summary card
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 1.2rem; border-radius: 10px; margin-bottom: 1.5rem;">
            <h3 style="color: white; margin: 0; font-size: 1.6rem;">
                {object_year} {object_brand} {object_model}
            </h3>
            <p style="color: #e8e8e8; margin: 0.3rem 0 0 0; font-size: 0.95rem;">
                {object_mileage:,} km • {object_fuel} • {object_transmission} • {object_drive}
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Main results container
    with st.container(border=True):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Trade-in Value", f"{CURRENCY}{trade_in_value:,}")
            st.caption("🔵 Quick sale estimate")
        
        with col2:
            st.metric("Market Estimate", f"{CURRENCY}{int(predicted_price):,}", 
                     delta=None, delta_color="off")
            st.caption("🎯 Fair market value")
        
        with col3:
            st.metric("Dealer Retail", f"{CURRENCY}{retail_value:,}")
            st.caption("🔴 Maximum retail price")
    
    # Mileage Impact Chart
    st.write("")
    st.write("### 📉 How Mileage Affects Value")
    
    # Generate predictions for different mileage values
    mileage_range = [0, 25000, 50000, 75000, 100000, 150000, 200000, 250000, 300000]
    predicted_prices = []
    
    for test_mileage in mileage_range:
        # Create test input with same values but different mileage
        test_input = pd.DataFrame([{
            'Year': object_year,
            'CarAge': CURRENT_YEAR - object_year,
            'Mileage(km)': test_mileage,
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
        
        # Apply same encoding
        test_encoded = pd.get_dummies(test_input)
        test_encoded = test_encoded.reindex(columns=trained_columns, fill_value=0)
        
        # Predict
        test_prediction = model.predict(test_encoded)
        predicted_prices.append(test_prediction[0])
    
    # Create the chart
    import plotly.graph_objects as go
    
    fig = go.Figure()
    
    # Add the line showing price vs mileage
    fig.add_trace(go.Scatter(
        x=mileage_range,
        y=predicted_prices,
        mode='lines',
        name='Estimated Value',
        line=dict(color='#667eea', width=3),
        hovertemplate='%{x:,} km<br>$%{y:,.0f}<extra></extra>'
    ))
    
    # Add a marker for the current vehicle
    current_index = mileage_range.index(min(mileage_range, key=lambda x: abs(x - object_mileage)))
    if abs(mileage_range[current_index] - object_mileage) > 10000:
        # If current mileage isn't close to any point, add it separately
        fig.add_trace(go.Scatter(
            x=[object_mileage],
            y=[predicted_price],
            mode='markers',
            name='Your Vehicle',
            marker=dict(color='#f5576c', size=15, symbol='star'),
            hovertemplate='Your Car<br>%{x:,} km<br>$%{y:,.0f}<extra></extra>'
        ))
    else:
        # Highlight the closest point
        fig.add_trace(go.Scatter(
            x=[mileage_range[current_index]],
            y=[predicted_prices[current_index]],
            mode='markers',
            name='Your Vehicle',
            marker=dict(color='#f5576c', size=15, symbol='star'),
            hovertemplate='Your Car<br>%{x:,} km<br>$%{y:,.0f}<extra></extra>'
        ))
    
    # Update layout
    fig.update_layout(
        xaxis_title="Mileage (km)",
        yaxis_title=f"Estimated Value ({CURRENCY})",
        hovermode='x unified',
        showlegend=True,
        height=400,
        margin=dict(l=20, r=20, t=20, b=20),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    
    # Change update_xaxis to update_xaxes
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')

    # Change update_yaxis to update_yaxes
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.caption(f"💡 This chart shows how your {object_brand} {object_model}'s value changes with mileage, keeping all other factors constant.")
    
    # Additional insights
    st.divider()
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.write("#### 📊 Key Factors")
        car_age = CURRENT_YEAR - object_year
        st.write(f"- **Age:** {car_age} years old")
        st.write(f"- **Mileage:** {object_mileage:,} km")
        st.write(f"- **Fuel Type:** {object_fuel}")
        st.write(f"- **Transmission:** {object_transmission}")
        st.write(f"- **Accident History:** {object_accident}")
    
    with col_right:
        st.write("#### 💡 Market Insights")
        
        if predicted_price > 50000:
            st.write("🟢 **Premium Segment** - This vehicle is in the luxury category")
        elif predicted_price > 25000:
            st.write("🟡 **Mid-Range Segment** - This vehicle offers good value")
        else:
            st.write("🔵 **Economy Segment** - This vehicle is budget-friendly")
        
        if object_accident == "Yes":
            st.write("⚠️ Accident history may reduce market appeal by 10-20%")
        
        if object_mileage > 150000:
            st.write("⚠️ High mileage (>150k km) may affect resale value")
        elif object_mileage < 30000:
            st.write("✅ Low mileage increases market desirability")
        
        if car_age < 3:
            st.write("✅ Recent model year commands premium pricing")
        elif car_age > 10:
            st.write("📉 Older vehicles typically depreciate faster")
    
    st.info(f"**Final Estimate: {CURRENCY}{int(predicted_price):,}**")
    st.caption("📌 **Disclaimer:** This is an AI-generated estimate based on historical data and machine learning models. Actual market prices may vary based on location, market conditions, vehicle specifics, and current demand.")

if st.button("Back to Homepage"):
    st.write("Redirecting to homepage...")
    st.switch_page("MainPage.py")
        
