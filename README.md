# AI-Powered Supply Chain Risk Prediction & Inventory Optimization System

## Overview

This project is a full-stack AI-driven supply chain analytics platform that predicts inventory demand, identifies supply chain risks, detects anomalies, and generates optimization recommendations for warehouses and retail operations.

The platform combines:
- Machine Learning
- Forecasting
- Risk Prediction
- Anomaly Detection
- Inventory Optimization
- Scenario Simulation
- Interactive Analytics Dashboards

into a production-style AI application.

---

# Features

## Inventory Demand Forecasting
- Product demand prediction
- Warehouse-level forecasting
- Regional demand analytics
- Seasonal demand analysis

## Supply Chain Risk Prediction
- Supplier delay prediction
- Inventory shortage risk
- Overstock detection
- Delivery bottleneck alerts
- Demand surge prediction

## AI-Based Inventory Optimization
- Reorder recommendations
- Safety stock suggestions
- Warehouse redistribution recommendations
- Dynamic inventory management

## Operational Anomaly Detection
- Inventory anomaly detection
- Sudden stock drop monitoring
- Supplier inconsistency detection
- Operational risk monitoring

## Scenario Simulation
- Revenue impact estimation
- Inventory shortage simulation
- Operational cost analysis
- Risk estimation under disruptions

## Analytics Dashboard
- KPI cards
- Forecast charts
- Pie charts
- Bar charts
- Alerts panel
- Live activity feed
- Simulation dashboard
- PDF export reports

---

# Tech Stack

## Backend
- Python
- FastAPI
- Scikit-learn
- Pandas
- NumPy

## Frontend
- React.js
- Axios
- Recharts

## Machine Learning
- Random Forest Regression
- Isolation Forest
- Risk Classification Logic

## Visualization
- Recharts
- Analytics Dashboards

---

# API Endpoints

## Forecast API
POST `/forecast`

## Risk Prediction API
POST `/predict-risk`

## Optimization API
POST `/optimize`

## Anomaly Detection API
POST `/detect-anomaly`

## Scenario Simulation API
POST `/simulate`

---

# Dashboard Features

- Enterprise Dashboard UI
- KPI Monitoring
- Forecast Analytics
- Warehouse Distribution Charts
- Regional Demand Analytics
- Supply Chain Alerts
- Real-Time Activity Feed
- PDF Report Export
- Loading & Error Handling

---

# Installation

## Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

## Frontend Setup

```bash
cd frontend

npm install

npm start
```

---

# Project Structure

```bash
AI-Powered-Supply-Chain-System/
│
├── backend/
│   ├── datasets/
│   ├── ml_models/
│   ├── main.py
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│
├── project_screenshots/
│
└── README.md
```

---

# Machine Learning Modules

## Forecasting Module
- Demand forecasting
- Inventory prediction
- Sales trend analysis

## Risk Prediction Module
- Supply chain risk analysis
- Supplier delay prediction
- Inventory shortage detection

## Optimization Engine
- Inventory recommendations
- Reorder optimization
- Warehouse balancing

## Anomaly Detection Module
- Isolation Forest detection
- Inventory anomaly monitoring
- Risk anomaly alerts

## Simulation Engine
- Revenue impact estimation
- Cost analysis
- Supply chain disruption simulation

---

# Future Improvements

- Prophet forecasting integration
- LSTM deep learning forecasting
- PostgreSQL integration
- Docker deployment
- Authentication system
- Real-time WebSocket monitoring
- Explainable AI integration
- Automated retraining pipelines

---

# Evaluation Highlights

This project demonstrates:
- Full-stack AI engineering
- Machine learning integration
- Forecasting systems
- Optimization engines
- Interactive dashboards
- Scalable backend APIs
- Analytics visualization
- Production-style architecture

---

# Author

Developed as part of an AI-powered supply chain analytics assignment.
