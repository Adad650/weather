import requests
import json

api_key = ("a1da61b6cb48fcc78c40eae7c0776c4b")

print("Enter location in this format [CityName,CountryCode]")
userCityOfChoice = input().strip()

locationURL = f"https://api.openweathermap.org/geo/1.0/direct?q={userCityOfChoice}&limit=1&appid={api_key}"
locationResponse = requests.get(locationURL)
locationData = locationResponse.json()

if not locationData:
    print("Location not found.")
    exit()

lat = locationData[0]['lat']
lon = locationData[0]['lon']

weatherURL = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max,rain_sum&timezone=auto&forecast_days=3"
weatherResponse = requests.get(weatherURL)
weatherData = weatherResponse.json()

dates = weatherData['daily']['time']
tempMin = weatherData['daily']['temperature_2m_min']
tempMax = weatherData['daily']['temperature_2m_max']

for i in range(3):
    print(f"For {dates[i]}: Low of {tempMin[i]}°C, High of {tempMax[i]}°C")