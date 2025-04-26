import re
import requests

# First, ask the user to provide the name of a city
# Since I am going to scrape on environment canada, there is no point in accepting a city that is not in Canada. 
# Hence the ",CA" additional input in the location URL string itself.
userCity = str(input("Enter Your Canadian City Of Choice:  "))

locationURL = f"https://api.openweathermap.org/geo/1.0/direct?q={userCity},CA&limit=1&appid=a1da61b6cb48fcc78c40eae7c0776c4b"


try:
    locationResponse = requests.get(locationURL)
    city = locationResponse.json()
    lat = city[0]['lat']
    lon = city[0]['lon']
except:
    print (f"Not a city, Learn to type. {userCity} is not even a city in Canada. READ THE COMMENTS.")
    exit()

countryOfCity = city[0]['country']
provinceOfCity = city[0]['state']
fullNameOfCity = city[0]['name']


# Now that I have a confirmed Canadian city with a legit lat / long, 
# How about I ask Env Canada aboot the weather ...
# he he he...
# (how smart of me)

url = f"https://weather.gc.ca/en/location/index.html?coords={lat},{lon}"

try:
    response = requests.get(url)
except:
    print (f"Something went wrong in retrieving the weather for {fullNameOfCity}, {provinceOfCity}, {countryOfCity}.")
    print ("Try again later")      
    exit()


weather = re.findall(r'data-v-7e10dc71><span data-v-7e10dc71>(\d+)°', response.text)
weatherLow = re.findall(r'Low [^0-9]*([+-]?\d+)', response.text)
weatherHigh = re.findall(r'High [^0-9]*([+-]?\d+)', response.text)
rain = re.findall(r'<small title="Chance of Precipitation"[^>]*>(\d+)%</small>', response.text)

# Changed the location of try and except to if and else

if rain != None and (len(rain)>0):
    chanceOfRainToday = rain[0]
    chanceOfRainTommorrow = rain[1]
else:
    chanceOfRainToday = 0
    chanceOfRainTommorrow = 0
    


print(f"Here is the weather of {fullNameOfCity}, {provinceOfCity}, {countryOfCity}:")
print(f"Current weather: {weather[0]}°C")
print(f"Today Low: {weatherLow[0]}°C")
print(f"Today High: {weatherHigh[0]}°C")
print(f"Tomorrow Low: {weatherLow[1]}°C")
print(f"Tomorrow High: {weatherHigh[1]}°C")
print(f"Rain Today: {chanceOfRainToday}%")
print(f"Rain Tommorrow: {chanceOfRainTommorrow}%")
    

