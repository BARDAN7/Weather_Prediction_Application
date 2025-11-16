#  🌤️  WEATHER PREDICTION SYSTEM

A machine-learning based weather forecasting tool using LightGBM (LGBM Classifier) and Streamlit for an interactive web interface. The system predicts weather conditions such as sunny, cloudy, overcast, or rainy using key environmental features.

<b> # 🚀  Features </b>

 Accurate Weather Prediction using LGBM Classifier
 Streamlit Web UI for user-friendly interaction
 Real-time Input Fields for weather variables
 Fast and lightweight model suitable for deployment
 Supports both real-time and manual data entry
 Displays prediction confidence (optional)
 
 # Input Parameters

The user can enter the following features in the Streamlit interface:

Temperature (°C)
Humidity (%)
Precipitation (%)
Wind Speed (km/h)
Location Type (inland, coastal, mountain)
Cloud Cover (clear, partly cloudy, cloudy, overcast)
Season (spring, summer, autumn, winter)
Visibility (optional)
Pressure (optional)

# 🧠  Model Details

Algorithm: LightGBM Classifier (LGBM)

Reason for using:

Fast training and prediction

Handles categorical & numerical data well

Excellent accuracy with low computational cost

Trained on labeled weather data with feature encoding for season, location, and cloud cover.

📦 Installation
pip install -r requirements.txt

Typical requirements:

lightgbm
streamlit
pandas
numpy
scikit-learn

▶️ Run the Application
streamlit run app.py

This will open the interactive prediction dashboard in your browser.

📚 How It Works

User enters weather-related parameters into Streamlit.
System preprocesses input and converts categories into numeric codes.
LGBM Classifier predicts the weather condition.
Streamlit displays the prediction on-screen.
