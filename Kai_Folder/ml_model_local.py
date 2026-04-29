import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score

# Daten laden die wir aus Kaggle.com (https://www.kaggle.com/datasets/ravishah1/carvana-predict-car-prices) haben, also lokales Datenmanagement.
df = pd.read_csv('carvana.csv')

def clean_and_train(data): #Datenbereinigung der Carvana Datenbank
    data['Year'] = data['Year'].astype(str).str[:4].astype(int) # Korrektur des Jahres: Nur die ersten 4 Ziffern extrahieren (z.B. 20173 -> 2017)
    
    # Umgang mit Preis-Ausreissern: Wir nutzen die Interquartilsabstand-Methode (IQR) : https://statologie.de/interquartilsabstand-python/
    Q1 = data['Price'].quantile(0.25)
    Q3 = data['Price'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    cleaned_data = data[(data['Price'] >= lower_bound) & (data['Price'] <= upper_bound)].copy() #Daten filtern (Cleaned Version existiert nur in dieser Variable)
    
    cleaned_data['Type'] = cleaned_data['Type'].fillna('Unknown')   #Fehlende Werte in 'Type' behandeln (z.B. durch 'Unknown' ersetzen)

    # Definition der Input/Output Variablen für das Modell
    X = cleaned_data[['Brand', 'Type', 'Year', 'Miles']]
    y = cleaned_data['Price']

    # Kategoriale Merkmale (Brand, Type) müssen in Zahlen umgewandelt werden
    categorical_features = ['Brand', 'Type']
    categorical_transformer = OneHotEncoder(handle_unknown='ignore') #https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', categorical_transformer, categorical_features)
        ], remainder='passthrough')

    # Erstellung der Pipeline: Vorverarbeitung + Modell
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    #ML Learning Algorithmus 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Starte Training...")
    model_pipeline.fit(X_train, y_train)

    # Validierung der Vorhersagegenauigkeit
    y_pred = model_pipeline.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    print(f"Modell erfolgreich trainiert.")
    print(f"Bestimmtheitsmass $R^2$: {r2:.4f}")
    print(f"Mittlerer absoluter Fehler (MAE): {mae:.2f} USD")

    # Modell für die Streamlit-App speichern
    with open('car_model.pkl', 'wb') as f:
        pickle.dump(model_pipeline, f)
    
    return model_pipeline

# Ausführung des Prozesses
trained_model = clean_and_train(df)