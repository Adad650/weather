import requests
import json
import mySecrets

data = []
#api_key = "insert your api key"
api_key = mySecrets.openWeatherApiKeyAdi

# ask the user which city they want the weather for
print("Enter location in this format [CityName, CountryName]")
userCityOfChoice = str(input())
# call openweather geocoding api to get lat / long of that city

locationURL = "https://api.openweathermap.org/geo/1.0/direct?q=" + userCityOfChoice + "&appid=a1da61b6cb48fcc78c40eae7c0776c4b"
locationURLResponse = requests.get(locationURL)
locationURLResponseJSON = json.loads(locationURLResponse.content)

lat = locationURLResponseJSON[0]['lat']
long = locationURLResponseJSON[0]['lon']

 #call weather api with the lat/long
weatherURL = "https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) + "&&longitude=" + str(long) + "&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max,rain_sum&timezone=America%2FNew_York&forecast_days=3"

plsGiveAnswer = requests.get(weatherURL)
TemperatureURLresponseJSON = json.loads(plsGiveAnswer.content)

dates = TemperatureURLresponseJSON['daily']['time']

day1 = dates[0]
day2 = dates[1]
day3 = dates[2]

tempMin = TemperatureURLresponseJSON['daily']['temperature_2m_min']
tempMinDay1 = tempMin[0]
tempMinDay2 = tempMin[1]
tempMinDay3 = tempMin[2]

tempMax = TemperatureURLresponseJSON['daily']['temperature_2m_max']
tempMaxday1 = tempMax[0]
tempMaxday2 = tempMax[1]
tempMaxday3 = tempMax[2]

print("For the day ", day1, "the forecast is between", tempMinDay1,"and ",tempMaxday1," Degrees Celsius")
print("For the day ", day2, "the forecast is between", tempMinDay2,"and ",tempMaxday2," Degrees Celsius")
print("For the day ", day3, "the forecast is between", tempMinDay3,"and ",tempMaxday3," Degrees Celsius")


