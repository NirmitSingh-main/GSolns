# 🚀 LogiRisk AI — Intelligent Supply Chain Risk Platform

> **A full-stack Decision Intelligence System** combining FastAPI, React/Vite, Machine Learning, and live geospatial APIs to optimize logistics routes, simulate environmental risks, and monitor an active shipment fleet in real time.

---

## 📌 Overview

LogiRisk AI is a production-grade supply chain analytics platform originally built as a Streamlit prototype and fully migrated to a modern **FastAPI + React (Vite)** architecture. The system ingests live weather conditions, estimates traffic intensity from system time, evaluates multiple route options through a trained ML model, and surfaces explainable risk scores to decision-makers in an interactive, auto-refreshing dashboard.

---

## 🎯 Key Features

| Feature | Details |
|---|---|
| **🗺️ Multi-Route Optimization** | Fetches 3 alternative routes via OpenRouteService, scores each with ML, and selects the optimal path |
| **🌦️ Live Weather Integration** | OpenWeather API provides real-time conditions per city (rain, haze, temperature) |
| **🚗 Automated Traffic Estimation** | System clock auto-infers peak/off-peak traffic — no manual dropdown |
| **🧠 ML Risk Scoring** | Pre-trained model scores each route on weather, traffic, temperature, and time of day |
| **🔍 Explainable AI (XAI)** | Every route displays human-readable "Intelligence Factors" explaining the risk score |
| **⚡ Hybrid Adaptive Learning** | Backend pseudo-learning adjusts risk weights based on detected traffic trends |
| **🗄️ Live SQLite Database** | Every optimization is logged; auto-purges at 300 records |
| **📊 Real-Time Analytics** | K-Means clustering + trend analysis on live DB data, auto-refreshing every 10s |
| **🔥 Geospatial Heatmap** | `leaflet.heat` renders India-wide ML risk density across 12 logistics hubs |
| **🚢 Fleet Portfolio Dashboard** | Live ML-scored shipment inventory with weather icons and delay reason per row |

---

## 🧠 System Workflow

```
System Clock → Traffic Estimate (Auto)
User Input (Source, Destination) → OpenWeather API (Live Weather + Temp)
                                 → OpenRouteService API (3 Alternative Routes)
                                         ↓
                          ML Model (risk score per route)
                                         ↓
                    Risk Appetite (λ) → Total Score = Duration + (λ × Risk)
                                         ↓
              Best Route Selected → Logged to SQLite DB → UI Updated
```

---

## 🧰 Tech Stack

### Backend
| Tool | Role |
|---|---|
| `FastAPI` | REST API framework |
| `Uvicorn` | ASGI server |
| `scikit-learn` | ML inference + K-Means clustering |
| `SQLite` | Live query database (logirisk.db) |
| `OpenWeather API` | Real-time weather per city |
| `OpenRouteService API` | Multi-route geospatial data |

### Frontend
| Tool | Role |
|---|---|
| `React + Vite` | UI framework + dev server |
| `React Router` | 4-page dashboard routing |
| `React-Leaflet + Leaflet` | Interactive geospatial maps |
| `leaflet.heat` | Risk density heatmap overlay |
| `Recharts` | Analytics & clustering charts |
| `Axios` | API communication |
| `Lucide React` | Icon library |

---

## 📁 Project Structure

```
GSolns/
│
├── main.py                     # FastAPI backend — all endpoints
├── requirements.txt            # Python dependencies
├── SETUP.md                    # Full setup guide
├── LogiRisk_Architecture_Overview.txt  # Technical architecture doc
├── logirisk.db                 # SQLite live database (auto-created)
├── .env                        # API keys (NOT committed)
│
├── utils/
│   ├── weather.py              # OpenWeather API with 5-min cache
│   └── route.py                # OpenRouteService with fallback routes
│
├── ml/
│   ├── inference/
│   │   └── predict.py          # ML model inference engine
│   ├── training/
│   │   └── train_model.py      # Model training script
│   └── models/
│       └── model.pkl           # Trained model binary
│
├── data/
│   ├── raw/                    # Raw datasets
│   └── processed/              # Processed training data
│
└── frontend/
    ├── package.json            # JS dependencies
    ├── src/
    │   ├── App.jsx             # Router + Leaflet CSS import
    │   ├── index.css           # Global dark/gold theme
    │   └── pages/
    │       ├── Portfolio.jsx   # Fleet dashboard (live DB + ML)
    │       ├── RouteOptimization.jsx  # Map + route comparison
    │       ├── Analytics.jsx   # Charts + clustering (auto-refresh)
    │       └── Simulation.jsx  # Heatmap risk simulation
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
VITE_OPENWEATHER_API_KEY=your_openweather_key_here
VITE_OPENROUTE_API_KEY=your_openrouteservice_key_here
```

Get free API keys from:
- [OpenWeather](https://openweathermap.org/api) — free tier, 60 calls/min
- [OpenRouteService](https://openrouteservice.org/) — free tier, 2000 calls/day

> ⚠️ Never commit your `.env` file — it is protected by `.gitignore`

---

## ⚙️ How to Run

### 1. Clone & setup environment
```bash
git clone <repo-url>
cd GSolns
```

### 2. Backend
```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload
# → API running at http://localhost:8000
```

### 3. Frontend
```bash
cd frontend
npm install
npm run dev -- --force
# → UI running at http://localhost:5173
```

---

## 📊 ML Model Details

- **Architecture**: Pre-trained classifier (trained on logistics delay dataset)
- **Features**: Weather condition, traffic level, temperature (°C), hour of day
- **Output**: Risk score (0–100) + classification (LOW / MEDIUM / HIGH)
- **Explainability**: Custom `explain_risk()` generates human-readable factor list per route
- **Adaptive Weighting**: Backend dynamically increases traffic penalty during consecutive high-traffic windows

---

## 🏁 Conclusion

LogiRisk AI demonstrates how real-time APIs, persistent databases, and ML explainability can be fused into a production-grade logistics intelligence platform — going well beyond a static prototype into a true decision-support system.
