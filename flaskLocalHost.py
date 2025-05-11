from flask import Flask, request
from datetime import datetime
import re
import requests
import mySecrets

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Canadian City Weather Lookup</h2>
        <form action="/weather">
            Enter Canadian city: <input type="text" name="city">
            <input type="submit" value="Get Weather">
        </form>
    '''

@app.route('/weather')
def weather():
    userCity = request.args.get('city')
    if not userCity:
        return "No city provided."

    locationURL = f"https://api.openweathermap.org/geo/1.0/direct?q={userCity},CA&limit=1&appid={mySecrets.apiKey}"
    try:
        city = requests.get(locationURL).json()
        lat = city[0]['lat']
        lon = city[0]['lon']
        countryOfCity = city[0]['country']
        provinceOfCity = city[0]['state']
        fullNameOfCity = city[0]['name']
    except:
        return f"""
            {userCity} isn't a valid Canadian city.
            To continue, please try again by going here.
            <a href="/">Home</a>
            """

    url = f"https://weather.gc.ca/en/location/index.html?coords={lat},{lon}"
    try:
        response = requests.get(url)
    except:
        return "Failed to fetch weather."

    weather = re.findall(r'data-v-7e10dc71><span data-v-7e10dc71>(\d+)°', response.text)
    weatherLow = re.findall(r'Low [^0-9]*([+-]?\d+)', response.text)
    weatherHigh = re.findall(r'High [^0-9]*([+-]?\d+)', response.text)
    rain = re.findall(r'<small title="Chance of Precipitation"[^>]*>(\d+)%</small>', response.text)

    if rain and len(rain) > 0:
        chanceOfRainToday = rain[0]
        chanceOfRainTommorrow = rain[1] if len(rain) > 1 else "0"
    else:
        chanceOfRainToday = "0"
        chanceOfRainTommorrow = "0"

    mississaugaLink = ""
    if fullNameOfCity.lower() != "mississauga":
        mississaugaLink = '<p><a href="/weather?city=Mississauga">Mississauga Weather</a></p>'

    return f"""
        <h2>Weather in {fullNameOfCity}, {provinceOfCity}, {countryOfCity}</h2>
        <p>Current: {weather[0]}°C</p>
        <p>Today Low: {weatherLow[0]}°C | High: {weatherHigh[0]}°C</p>
        <p>Tomorrow Low: {weatherLow[1]}°C | High: {weatherHigh[1]}°C</p>
        <p>Rain Today: {chanceOfRainToday}%</p>
        <p>Rain Tomorrow: {chanceOfRainTommorrow}%</p>
        <p>
        {mississaugaLink}
        <a href="/">Check another city</a>
    """
@app.route('/time')
def timeRightNow():
    nowTime = datetime.now()
    currentTime = nowTime.strftime("%H:%M")
    returnValueString = f"""
        <h2>Current Time</h2>
        <p>The current time is: {currentTime}</p>
    """
    return returnValueString



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)


