# 🚀 Real-Time Risk Scoring Dashboard for Supply Chain

## 📌 Overview

This project is a real-time risk prediction system designed to improve supply chain decision-making. It combines machine learning, live weather data, and route analytics to estimate delivery risks and provide actionable insights.

The system continuously evaluates shipment conditions and outputs a risk score (0–100) along with recommendations to help prevent delays.

## 🎯 Key Features

- **🔴 Dynamic Risk Scoring**: Calculates real-time risk scores based on environmental and operational factors.
- **🌦️ Weather Integration (API-based)**: Fetches live weather conditions (temperature, conditions, coordinates).
- **🗺️ Route Intelligence**: Estimates distance and travel time using routing APIs.
- **🧠 Machine Learning Prediction**: Uses a trained Random Forest model to predict delay probability.
- **📊 Explainable Insights**: Shows contributing factors such as weather, traffic, and time.
- **🚨 Smart Alerts & Recommendations**: Provides decision support:
  - Low Risk → Proceed
  - Medium Risk → Monitor
  - High Risk → Delay / Reroute
- **📈 Risk Trend Visualization**: Displays simulated trends to understand risk evolution.
- **📍 Multi-Input Dashboard (Streamlit UI)**: Simple interface to test different routes and scenarios.

## 🧠 System Workflow

```
User Input (Source, Destination, Traffic)
            ↓
Weather API → (Weather, Temp, Coordinates)
            ↓
Route API → (Distance, Duration)
            ↓
ML Model → (Delay Probability)
            ↓
Risk Score (0–100) + Risk Level
            ↓
Dashboard Visualization + Recommendations
```

## 🧰 Tech Stack

**Backend & ML**
- Python
- Pandas, NumPy
- Scikit-learn (Random Forest)

**APIs**
- OpenWeather API
- OpenRouteService API

**Frontend (Current)**
- Streamlit

**Visualization**
- Matplotlib
- PyDeck / Streamlit Maps

## 📊 Machine Learning Details

**Model**: Random Forest Classifier

**Features**:
- Weather condition
- Traffic level
- Temperature
- Time of day

**Output**:
- Delay probability
- Risk score (0–100)
- Risk classification

## 📁 Project Structure

```
gslns/
│
├── app.py                  # Streamlit dashboard
├── requirements.txt
│
├── utils/
│   ├── weather.py          # Weather API logic
│   ├── route.py            # Routing API logic
│
├── ml/
│   ├── inference/
│   │   └── predict.py      # Model inference
│   ├── training/
│   │   └── train_model.py
│   └── models/
│       └── model.pkl
│
├── data/
│   ├── raw/
│   └── processed/
```

## 🔑 API Configuration

This project requires API keys from two external services. Follow these steps to set them up:

### 1. OpenWeather API
1. Visit [OpenWeather](https://openweathermap.org/api)
2. Sign up for a free account
3. Generate an API key from your dashboard
4. Copy your API key

### 2. OpenRouteService API
1. Visit [OpenRouteService](https://openrouteservice.org/)
2. Sign up for a free account
3. Generate an API key from your dashboard
4. Copy your API key

### 3. Create `.env` File
Create a `.env` file in the project root directory with the following content:

```env
OPENWEATHER_API_KEY=your_openweather_api_key_here
OPENROUTE_API_KEY=your_openroute_api_key_here
```

Replace `your_openweather_api_key_here` and `your_openroute_api_key_here` with your actual API keys.

## ⚙️ How to Run

1. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

2. **Set up your `.env` file** with API keys (see section above)

3. **Run the Streamlit app**:
   ```sh
   streamlit run app.py
   ```

4. **Open your browser** and navigate to:
   ```
   http://localhost:8501
   ```

## 🔮 Future Enhancements

- 🌐 Full-stack migration (React + FastAPI)
- 🗺️ Real route path visualization (polyline rendering)
- 🔁 Multi-route comparison (fastest vs safest)
- 📱 Mobile-friendly interface
- 🧠 Advanced models (XGBoost / RL-based routing)

## 🏁 Conclusion

This project demonstrates how AI + real-time data can be combined to build intelligent systems for supply chain optimization. It provides a practical approach to predicting delays, assessing risks, and improving logistics efficiency.
