from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sklearn.ensemble import (
    RandomForestRegressor,
    RandomForestClassifier,
    IsolationForest
)

from ml_models.preprocessing import load_data

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# =========================================
# LOAD DATASET
# =========================================

df = load_data()

# =========================================
# FORECASTING MODEL
# =========================================

forecast_X = df[[
    "stock_level",
    "supplier_lead_time",
    "promotion",
    "holiday"
]]

forecast_y = df["sales"]

forecast_model = RandomForestRegressor()

forecast_model.fit(forecast_X, forecast_y)

# =========================================
# RISK PREDICTION MODEL
# =========================================

risk_X = df[[
    "stock_level",
    "supplier_lead_time",
    "promotion",
    "holiday"
]]

risk_y = df["risk"]

risk_model = RandomForestClassifier()

risk_model.fit(risk_X, risk_y)

# =========================================
# ANOMALY DETECTION MODEL
# =========================================

anomaly_features = df[[
    "sales",
    "stock_level",
    "supplier_lead_time"
]]

anomaly_model = IsolationForest(
    contamination=0.1,
    random_state=42
)

anomaly_model.fit(anomaly_features)

# =========================================
# REQUEST SCHEMAS
# =========================================

class ForecastRequest(BaseModel):
    stock_level: int
    supplier_lead_time: int
    promotion: int
    holiday: int

class AnomalyRequest(BaseModel):
    sales: int
    stock_level: int
    supplier_lead_time: int

# =========================================
# HOME API
# =========================================

@app.get("/")
def home():
    return {
        "message": "Supply Chain AI Backend Running"
    }

# =========================================
# FORECAST API
# =========================================

@app.post("/forecast")
def forecast(data: ForecastRequest):

    prediction = forecast_model.predict([[
        data.stock_level,
        data.supplier_lead_time,
        data.promotion,
        data.holiday
    ]])

    return {
        "predicted_sales": round(prediction[0], 2)
    }

# =========================================
# RISK PREDICTION API
# =========================================

@app.post("/predict-risk")
def predict_risk(data: ForecastRequest):

    prediction = risk_model.predict([[
        data.stock_level,
        data.supplier_lead_time,
        data.promotion,
        data.holiday
    ]])

    return {
        "risk_level": prediction[0]
    }

# =========================================
# INVENTORY OPTIMIZATION API
# =========================================

@app.post("/optimize")
def optimize_inventory(data: ForecastRequest):

    recommendation = []

    # Low stock
    if data.stock_level < 300:
        recommendation.append(
            "Reorder inventory immediately"
        )

    # Supplier delay
    if data.supplier_lead_time > 7:
        recommendation.append(
            "Increase safety stock"
        )

    # Promotion demand
    if data.promotion == 1:
        recommendation.append(
            "Prepare for increased demand"
        )

    # Holiday demand
    if data.holiday == 1:
        recommendation.append(
            "Increase warehouse inventory for holiday demand"
        )

    # Default response
    if not recommendation:
        recommendation.append(
            "Inventory levels are optimized"
        )

    return {
        "recommendations": recommendation
    }

# =========================================
# ANOMALY DETECTION API
# =========================================

@app.post("/detect-anomaly")
def detect_anomaly(data: AnomalyRequest):

    prediction = anomaly_model.predict([[
        data.sales,
        data.stock_level,
        data.supplier_lead_time
    ]])

    if prediction[0] == -1:
        result = "Anomaly Detected"
    else:
        result = "Normal Operation"

    return {
        "status": result
    }
    
    
@app.post("/simulate")
def simulate_scenario(data: ForecastRequest):

    revenue_impact = 0
    shortage_risk = "Low"
    operational_cost = 1000

    # Demand surge simulation
    if data.promotion == 1:
        revenue_impact += 5000
        shortage_risk = "Medium"

    # Supplier delay simulation
    if data.supplier_lead_time > 7:
        operational_cost += 2000
        shortage_risk = "High"

    # Low inventory simulation
    if data.stock_level < 200:
        revenue_impact -= 3000
        shortage_risk = "High"

    return {
        "estimated_revenue_impact": revenue_impact,
        "inventory_shortage_risk": shortage_risk,
        "estimated_operational_cost": operational_cost
    }