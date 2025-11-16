import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Weather Prediction App", layout="centered")

# Load model
model = joblib.load("gbm_model.pt")

st.title("🌦️ Weather Prediction App")
st.write("Fill in the details below to predict the **Weather Type**")

# -------------------------
# ENCODING MAPPINGS (Based on your dataset)
# -------------------------

cloud_map = {'partly cloudy': 1, 'clear': 2, 'overcast': 3, 'cloudy': 4}
season_map = {'Winter': 1, 'Spring': 2, 'Summer': 3, 'Autumn': 4}
location_map = {'inland': 1, 'mountain': 2, 'coastal': 3}
reverse_weather_type = {0: 'Rainy', 1: 'Cloudy', 2: 'Sunny', 3: 'Snowy'}  # For displaying prediction

# -------------------------
# UI INPUTS
# -------------------------

temperature = st.number_input("Temperature (°C)", step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
wind_speed = st.number_input("Wind Speed (km/h)", step=0.1)
precipitation = st.number_input("Precipitation (%)", min_value=0.0, max_value=100.0, step=0.1)

cloud_cover = st.selectbox("Cloud Cover", list(cloud_map.keys()))
pressure = st.number_input("Atmospheric Pressure (hPa)", step=0.1)
uv_index = st.number_input("UV Index", min_value=0.0, max_value=15.0, step=0.1)
season = st.selectbox("Season", list(season_map.keys()))
visibility = st.number_input("Visibility (km)", step=0.1)
location = st.selectbox("Location", list(location_map.keys()))


# Convert text selections to numeric (same as dataset)
cloud_val = cloud_map[cloud_cover]
season_val = season_map[season]
location_val = location_map[location]

# -------------------------
# PREDICTION
# -------------------------
if st.button("Predict Weather Type"):
    
    input_data = np.array([[temperature, humidity, wind_speed, precipitation,
                            cloud_val, pressure, uv_index, season_val,
                            visibility, location_val]])

    prediction = model.predict(input_data)[0]
    weather_label = reverse_weather_type[prediction]

    st.success(f"🌦️ Predicted Weather Type: **{weather_label}**")


# Footer
st.markdown(
    "<hr><center>Developed with ❤️ using Streamlit</center>",
    unsafe_allow_html=True,
)
