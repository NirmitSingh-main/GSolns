import pickle
import pandas as pd

# -----------------------------
# Load model + encoders
# -----------------------------
with open("ml/models/model.pkl", "rb") as f:
    model, le_weather, le_traffic = pickle.load(f)

# -----------------------------
# Risk Level Helper
# -----------------------------
def get_risk_level(score):
    if score < 30:
        return "Low 🟢"
    elif score < 70:
        return "Medium 🟡"
    else:
        return "High 🔴"

# -----------------------------
# Safe Encoding
# -----------------------------
def safe_encode(encoder, value):
    value = value.lower()
    if value not in encoder.classes_:
        return 0
    return encoder.transform([value])[0]

# -----------------------------
# Prediction Function
# -----------------------------
def predict_delay(weather, traffic, temp, hour):
    try:
        weather = weather.lower()
        traffic = traffic.lower()

        weather_encoded = safe_encode(le_weather, weather)
        traffic_encoded = safe_encode(le_traffic, traffic)

        X = pd.DataFrame([{
            "weather": weather_encoded,
            "traffic": traffic_encoded,
            "temp": temp,
            "hour": hour
        }])

        delay_prob = model.predict_proba(X)[0][1]

        # 🔥 Controlled adjustment
        adjustment = 0

        if traffic == "low":
            adjustment -= 0.05
        elif traffic == "high":
            adjustment += 0.1

        if weather in ["rain", "snow", "thunderstorm", "drizzle"]:
            adjustment += 0.1

        
        #weighted combination
        adjusted_prob = delay_prob + adjustment
        delay_prob = (0.8 * delay_prob) + (0.2 * (delay_prob + adjusted_prob))
        #clamp safely
        delay_prob = max(0.05, min(0.95, delay_prob))

        risk_score = int(delay_prob * 100)
        risk_level = get_risk_level(risk_score)

        return {
            "delay_probability": delay_prob,
            "risk_score": risk_score,
            "risk_level": risk_level
        }

    except Exception as e:
        return {
            "delay_probability": 0.5,
            "risk_score": 50,
            "risk_level": "Unknown ⚠️",
            "error": str(e)
        }