import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import pickle

# Loading the data from the dataset from the correct folder
print("Lade Daten...")
df = pd.read_csv("ML/car_price_dataset.csv")

# Filtering the dataset to only keep the relevant columns
cols = ['Price($)', 'Brand', 'Model', 'Year', 'CarAge', 'Condition', 'Mileage(km)', 'EngineSize(L)', 'FuelType', 'Horsepower', 'Torque', 'Transmission', 'DriveType', 'BodyType', 'AccidentHistory'] 
df = df[cols]

# filtering und removing entries that don't make sense
df = df[df['Price($)'] > 500] # filter entries with a price below 500
df = df[df['Price($)'] < 300000] # filter entries with a price above 300k
df = df[df['Mileage(km)'] >= 0] # filter entries with negative mileage
df = df.dropna(subset=['Price($)', 'Mileage(km)', 'Brand', 'Model'])

print(f"Einträge nach Bereinigung: {df.shape[0]}")

# Encoding categorical columns into dummy variables for the model
df_encoded = pd.get_dummies(df, columns=['Brand', 'Model', 'Condition', 'FuelType', 'Transmission', 'DriveType', 'BodyType', 'AccidentHistory'])

# Separating the price as target, everything else are the features
X = df_encoded.drop('Price($)', axis=1)
y = df_encoded['Price($)']

# Train/Test Split: 80% for training, 20% for testing, 80/20 split allows a more precise modell while still having enought for testing with total of 50'000 datapoints
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the model
print("Trainiere Modell...")
model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Checking how well the model performs on the test data
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
r2  = r2_score(y_test, predictions)

print(f"Durchschnittlicher Fehler: ${mae:.0f}")
print(f"R²-Score: {r2:.4f}") 
print(f"Erklärte Varianz: {r2*100:.1f}%")

# Saving the model as a pickle file so we can load it in the app
with open('ML/model.pkl', 'wb') as f:
    pickle.dump((model, X.columns.tolist()), f)

print("Modell gespeichert!")
