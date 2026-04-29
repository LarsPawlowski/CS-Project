import streamlit as st

# 1. Page Configuration --> for the name of the tab
st.set_page_config(
    page_title="AutoAppraise - Your Car's True Value", 
    page_icon="🏎️",
    layout="centered" # "centered" looks better for landing pages than "wide"
)

# --- Quick Welcome Toast ---
# --- Little popup which can be closed ---
st.toast('Welcome to AutoAppraise', icon='🏎️')

# --- Sidebar Menu ---
# A sidebar in the website adds a multi-page dashboard --> allows to play between different codes
with st.sidebar:
    st.title("🏎️ AutoAppraise")
    st.markdown("Your car valuation expert.")
    st.divider()
    st.markdown("📍 **University of St. Gallen**")
    st.markdown("📚 FCS-BWL FS26")
    st.markdown("🐐 Team 1.10")

# --- Image Banner ---
# Using a high-quality stock photo from Unsplash. 
# Can be replaced by  downloaded, but downloaded photo has to be on the folder of autopraise
st.image("https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?q=80&w=1000&auto=format&fit=crop", use_container_width=True)

# 2. Hero Section
# basically the title section ==> maybe can add a slogan or something
st.title("🏎️ AutoAppraise")
st.subheader("Discover your car's *true* market value.")
st.markdown("""
Welcome to AutoAppraise! Enter your car's details and get an instant, data-driven price estimate. 
Our tool is powered by real market data to give you a fair valuation.
""")

# The Business Case (Requirement 1) --> we need a problem and solution section
st.write("---")
st.subheader("💡 The Business Case")
st.markdown("""
**The Problem:** Automotive market suffers from lack of...

**Our Solution:** What we do is...
""")
st.write("---")

# A primary button which when called sends to valuation page tab.
if st.button("Get your valuation 🚀", type="primary"):
    # This tells Streamlit to navigate to the other file!
    st.switch_page("pages/kai_input.py") 

st.divider() # Creates a clean horizontal line

# 3. Stats Section (Using native Streamlit metrics)
st.subheader("Our Numbers")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Prediction Accuracy", value="~94%")
with col2:
    st.metric(label="Cross-reference Data", value="5k+ cars")
with col3:
    st.metric(label="Valuation Time", value="< 5s")

st.divider()

# 4. "How it Works" Section (Using columns and info boxes to explain the simulation)
st.subheader("How the process works")
step1, step2, step3 = st.columns(3)

with step1:
    st.info("**01. Enter Details** \n\n Brand, model, year, mileage, and condition.")

with step2:
    st.info("**02. Cross-Reference** \n\n Live market listings and historical sales data.")

with step3:
    st.info("**03. Receive Your Valuation** \n\n Predicted fair value with a confidence range.")

st.divider()

# Video Section (which can be incorporated) ---
# Embedding video directly into website. --> place into the folder required.
st.subheader("Project Pitch")
st.markdown("Watch our 4-minute presentation on how AutoAppraise works:")
# you can do: st.video("my_presentation.mp4")
st.video("trial.MP4")

# 5. Features Section
# same way how 3,4 is)
st.subheader("What's under the hood")
feat1, feat2 = st.columns(2)

with feat1:
    st.markdown("📊 **Data Visualisation:** \nPrice trends and depreciation curves.")
    st.markdown("🔌 **Live API Data:** \nConnected to real car listing databases.")

with feat2:
    st.markdown("🤖 **Machine Learning:** \nTrained on thousands of real sales.")
    st.markdown("💾 **Database Storage:** \nSave and revisit past valuations.")

# --- Expanders for extra professional polish ---
st.subheader("More Information")

with st.expander("❓ Frequently Asked Questions"):
    st.write("**Where do you get your data?**\nWe cross-reference live market listings and historical sales.")
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

# 6.  Footer
st.caption("AutoAppraise · Built for the FCS-BWL Group Project · University of St. Gallen FS26")
