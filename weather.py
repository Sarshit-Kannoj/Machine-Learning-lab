
# Weetather Dataset - Machine Learning Lab

import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 22.7196,
    "longitude": 75.8577,
    "hourly": "temperature_2m,relative_humidity_2m",
    "forecast_days": 1
}

response = requests.get(url, params=params)
response.raise_for_status()
data = response.json()

df = pd.DataFrame({
    "Time": data["hourly"]["time"],
    "Temperature_C": data["hourly"]["temperature_2m"],
    "Humidity_Percent": data["hourly"]["relative_humidity_2m"]
})

df.to_csv("weather_dataset.csv", index=False)

print("Weather Dataset")
print(df.head())
print("\nDataset saved successfully as weather_dataset.csv")
