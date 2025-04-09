import streamlit as st
import joblib
import re

# Load model
model = joblib.load("phishing_model .pkl")

# URL feature extractor (simple example)
def extract_features(url):
    features = []
    features.append(len(url))                    # Length of URL
    features.append(url.count('@'))              # @ symbol
    features.append(url.count('https'))          # 'https' count
    features.append(url.count('.'))              # Dot count
    return [features]

# Streamlit UI
st.title("🔍 SafeLink Phishing URL Detector")

url_input = st.text_input("Enter a URL to check:", "")

if st.button("Check Now"):
    if url_input:
        features = extract_features(url_input)
        prediction = model.predict(features)[0]
        result = "⚠️ Phishing URL" if prediction == 1 else "✅ Safe URL"
        st.success(f"Prediction: {result}")
    else:
        st.warning("Please enter a URL.")
