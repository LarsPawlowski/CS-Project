import streamlit as st
import pandas as pd

# Title of the tab of the website
st.set_page_config(
    page_title="AutoAppraise - Your Car's True Value", 
    page_icon="🏎️",
    layout="centered" # "centered" looks better for landing pages than "wide"
)

# Little popup which can be closed on the right
st.toast('Welcome to AutoAppraise', icon='🏎️')

# A sidebar on the left side of the page, allowing you to switch easily between the different website tabs. 
with st.sidebar:
    st.title("🏎️ AutoAppraise")
    st.markdown("Your car valuation expert.")
    st.divider()
    st.markdown("📍 **University of St. Gallen**")
    st.markdown("📚 FCS-BWL FS26")
    st.markdown("🐐 Team 10.10")

# Using a stock photo from Unsplash. 
# Can be replaced by downloaded picture, but downloaded photo must be in the right folder.
# This is just a link which also works. On the top of the page as now we are going with the formatting, starting from the top down.
st.image("https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?q=80&w=1000&auto=format&fit=crop", use_container_width=True)

# The title section ==> maybe can add a slogan or something
# using ** for italics
st.title("🏎️ AutoAppraise")
st.subheader("Discover your car's *true* market value.")
st.markdown("""
Welcome to AutoAppraise! Enter your car's details and get an instant, data-driven price estimate. 
Our tool is powered by real market data to give you a fair valuation.
""")

# Here just describing the case at hand, describing the problem and the solution
# using ** ** for bold
st.write("---")
st.subheader("💡 The Business Case")
st.markdown("""
**The Problem:** The used car market suffers from heavy information asymmetry. Purchasers, lacking access to crucial information, such as accident history, are constantly vulnerable to high subjective pricing. This makes it incredibly difficult to determine a car's true value without specialized industry knowledge. 

**Our Solution:** AutoAppraise eliminates the guesswork from car buying. By cross-referencing your vehicle's specific details with thousands of historical sales data, our website computes an objective, data-driven price. This way we provide and empower you to make informed financial decisions backed by real market analytics.
""")
st.write("---")


# Making virtual columns, in which the buttons, which will direct to the seperate sections of the websites will be located.
# Making two columns, spaces two buttons equally. 

col1, col2 = st.columns(2)

with col1:
    if st.button("Get your valuation 🚀", type="primary", use_container_width=True): #primary button just makes it red background button, you can also use secondary etc...
        st.switch_page("pages/Appraisal.py") # changes to the other sections of the website, by changing to seperate code. This means that the code has to be found in the pages folder inside the CS main folder. 

with col2:
    if st.button("Add your car data 📊", type="primary", use_container_width=True):
        st.switch_page("pages/AddData.py")

st.divider() # Creates a clean horizontal line

# Stats Section (Using Streamlit metrics)
st.subheader("Our Numbers")
col1, col2, col3 = st.columns(3) # Here we made 3 coulumns instead

# Live counting logic, so that the code here reads the input added onto the car_price_dataset.csv, and counts that code, and the number will then be added onto the main page. --> live ticker 
try:
    df = pd.read_csv("ML/car_price_dataset.csv")
    total_cars = len(df)
    # This automatically adds a comma to big numbers (e.g., 50,001 cars)
    live_car_count = f"{total_cars:,} cars" 
except FileNotFoundError:
    # Just in case the file gets moved, it won't crash the app
    live_car_count = "Loading..." 

with col1:
    st.metric(label="Prediction Accuracy", value="~98%")#estimate
with col2:
    # Notice we removed "5k+ cars" and put our dynamic variable here!
    st.metric(label="Cross-reference Data", value=live_car_count) #from definition above
with col3:
    st.metric(label="Valuation Time", value="< 2s") #estimate


st.divider()

# Working with columns again to explain the process of estimating a car price
st.subheader("How the process works")
step1, step2, step3 = st.columns(3)

with step1:
    st.info("**01. Enter Details** \n\n Brand, model, year, mileage, condition, and more.") #working with infoboxes, to get th color in the back

with step2:
    st.info("**02. Cross-Reference** \n\n Live market listings and historical sales data.")

with step3:
    st.info("**03. Receive Your Valuation** \n\n Predicted fair value with a confidence range.")

st.divider()

# Idea of incorporating the video into the website itself, as the video should be not only like a teaser, but also another form of explanation
# The video has to be in the folder as well in your pages folder. And the file must be saved as an MP4. 
st.subheader("Project Pitch")
st.markdown("Watch our 4-minute presentation on how AutoAppraise works:")
st.video("video.mp4")

# Features Section similar to sections above with columns.

st.subheader("What's under the hood")
feat1, feat2 = st.columns(2)

with feat1:
    st.markdown("📊 **Data Visualisation:** \nPrice trends and depreciation curves.") #basically just more information, with new line.

with feat2:
    st.markdown("🤖 **Machine Learning:** \nTrained on thousands of real sales.")

#Expanders meaning once pressed more information will follow. 
st.subheader("More Information")

with st.expander("❓ Frequently Asked Questions"):
    st.write("**Where do you get your data?**\nWe used a free Dataset to train our model: https://www.kaggle.com/datasets/mahdimashayekhi/used-car-price")
    st.write("**Is this free?**\nYes! AutoAppraise is a free tool, everyone is welcome.")

with st.expander("👥 About the Team & Project"):
    st.write("Built for the Group Project at the University of St. Gallen.")
    st.write("---")
    st.write("**Contribution Matrix:**")
    st.write("- **Daniel:** Frontend Design & App Structure")
    st.write("- **Lars:** Linking Brand to Model to Year")
    st.write("- **Jovin:** Determining Reasonable Limitation Criteria Based on Datasets")
    st.write("- **Kai:** Machine Learning and Car Datasets")
    st.write("- **Roope:** Results page, Design & Structure")


st.write("") # Adds a little blank space

#Footer section using caption function
st.caption("AutoAppraise · Built for the FCS-BWL Group Project · University of St. Gallen FS26")
