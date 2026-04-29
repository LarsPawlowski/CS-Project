import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Gebrauchtwagen Preis-Predictor", layout="centered")

# Daten laden, um dynamische Filter zu ermöglichen
@st.cache_data
def get_mapping_data(): # Daten Laden damit wir später die Auto Typen mit der jeweiligen Marke verknüpfen können
    df = pd.read_csv('carvana_split.csv')
    df['Type'] = df['Type'].fillna('Unknown') # Füllen der leeren Daten typen.
    return df

# ML-Modell laden
@st.cache_resource
def load_trained_model():
    with open('car_model.pkl', 'rb') as f:
        return pickle.load(f)

df_mapping = get_mapping_data()
model = load_trained_model()

# App Page
st.title("🚗 Auto-Preis Schätzer (Dynamisch)")

st.header("Fahrzeugdaten eingeben")
col1, col2 = st.columns(2)

with col1:
    available_brands = sorted(df_mapping['Brand'].unique())
    brand = st.selectbox("Marke auswählen", available_brands)
    year_input = st.number_input("Baujahr", min_value=1990, max_value=2026, value=2018)

with col2:
    specific_types = df_mapping[df_mapping['Brand'] == brand]['Type'].unique() # Filter, sodass nur Typen angezeigt werden, die für die gewählte Marke existieren
    car_type = st.selectbox("Fahrzeugtyp (passend zur Marke)", sorted(specific_types))
    miles = st.slider("Meilenstand (Miles)", 0, 300000, 50000)

# --- VORHERSAGE ---
if st.button("Preis jetzt berechnen"):
    # Eingabedaten für das Modell vorbereiten
    input_data = pd.DataFrame({
        'Brand': [brand],
        'Type': [car_type],
        'Year': [int(str(year_input)[:4])], # Jahr ist wieder korrigiert
        'Miles': [miles]
    })

    try:
        prediction = model.predict(input_data)
        st.success(f"### Der geschätzte Preis beträgt: ${prediction[0]:,.2f}")
        
        # Visuelles Feedback zur Einordnung
        st.metric(label="Geschätzter Marktwert", value=f"${prediction[0]:,.2f}")
        
    except Exception as e:
        st.error(f"Fehler bei der Vorhersage: {e}")

# --- DOKUMENTATION (Punkt 6 & 7) ---
# with st.expander("Technisches Protokoll & Team"):
#    st.write("Die Fahrzeugtypen werden dynamisch basierend auf der 'Brand'-Spalte der Datenbank gefiltert.")