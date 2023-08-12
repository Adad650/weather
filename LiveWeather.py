import requests
import json
import secrets

data = []
#api_key = "insert your api key"
api_key = secrets.openWeatherApiKeyAdi

# ask the user which city they want the weather for

# call openweather geocoding api to get lat / long of that city


# ask the lat/long that the user wants the weather of ...
print("Please enter your latitude and longitude below there is no need to add N, W, S, or E\nFirst enter the longitude then the latitude")
long = str(input())
print("And your latitude.")
lat = str(input())

# call weather api with the lat/long
url = ('https://api.open-meteo.com/v1/forecast?latitude=' + lat +
       '&&longitude=' + long +
       '&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,'
       'uv_index_max,rain_sum&timezone=America%2FNew_York&forecast_days=3')


r = requests.get(url)
answer=json.loads(r.content)

dates = answer['daily']['time']

day1 = dates[0]
day2 = dates[1]
day3 = dates[2]

tempMin = answer['daily']['temperature_2m_min']
tempMinDay1 = tempMin[0]
tempMinDay2 = tempMin[1]
tempMinDay3 = tempMin[2]

tempMax = answer['daily']['temperature_2m_max']
tempMaxday1 = tempMax[0]
tempMaxday2 = tempMax[1]
tempMaxday3 = tempMax[2]

print("For the day ", day1, "the forecast is between", tempMinDay1,"and ",tempMaxday1," Degrees Celsius")
print("For the day ", day2, "the forecast is between", tempMinDay2,"and ",tempMaxday2," Degrees Celsius")
print("For the day ", day3, "the forecast is between", tempMinDay3,"and ",tempMaxday3," Degrees Celsius")


