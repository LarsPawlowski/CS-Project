import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import pickle

# Daten laden
print("Lade Daten...")
df = pd.read_csv("car_price_dataset.csv")

# Relevante Spalten behalten
cols = ['Price($)', 'Brand', 'Model', 'Year', 'CarAge', 'Condition', 
        'Mileage(km)', 'EngineSize(L)', 'FuelType', 'Horsepower', 
        'Torque', 'Transmission', 'DriveType', 'BodyType', 'AccidentHistory']
df = df[cols]

# Bereinigen
df = df[df['Price($)'] > 500]
df = df[df['Price($)'] < 300000]
df = df[df['Mileage(km)'] >= 0]
df = df.dropna(subset=['Price($)', 'Mileage(km)', 'Brand', 'Model'])

print(f"Einträge nach Bereinigung: {df.shape[0]}")

# Kategorische Spalten in Zahlen umwandeln
df_encoded = pd.get_dummies(df, columns=['Brand', 'Model', 'Condition', 
                                          'FuelType', 'Transmission', 
                                          'DriveType', 'BodyType', 
                                          'AccidentHistory'])

# Features und Zielwert trennen
X = df_encoded.drop('Price($)', axis=1)
y = df_encoded['Price($)']

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modell trainieren
print("Trainiere Modell...")
model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Genauigkeit prüfen
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f"Durchschnittlicher Fehler: ${mae:.0f}")

# Modell speichern
with open('model.pkl', 'wb') as f:
    pickle.dump((model, X.columns.tolist()), f)

print("Modell gespeichert!")
