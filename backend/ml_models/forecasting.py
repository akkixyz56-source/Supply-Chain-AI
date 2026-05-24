import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from preprocessing import load_data

# Load dataset
df = load_data()

# Features
X = df[["stock_level", "supplier_lead_time", "promotion", "holiday"]]

# Target
y = df["sales"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
mae = mean_absolute_error(y_test, predictions)

print("Predictions:", predictions)
print("MAE:", mae)