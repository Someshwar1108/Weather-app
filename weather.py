from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

API_KEY = "d41f96e1e"
CURRENT_WEATHER_URL = "http://api.weatherapi.com/v1/current.json"
FORECAST_URL = "http://api.weatherapi.com/v1/forecast.json"

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Weather Forecast App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <img src="https://res.cloudinary.com/dwkoy5wtd/image/upload/v1748721579/ChatGPT_Image_May_31_2025_at_05_37_04_AM_yj3ery.png" alt="Weather Logo"/>
        <h1 class= "title">GLOBAL WEATHER</h1>
    </header>
    <div class ="context">
        <div class = "weather-box">
            <div>
                <h1>Check Current Weather</h1>
                <form method="POST">
                    <input type="text" name="location" placeholder="Enter City or Zip Code" required>
                    <button type="submit">Get Weather</button>
                </form>
                {% if temperature %}
                <div class="result">
                    Current temperature in <strong>{{ location }}</strong> is <strong>{{ temperature }}°C</strong>
                </div>
                {% endif %}
            </div>
        </div>
        <div>
            {% if forecast %}
            <h2>5-Day Forecast</h2>
            <div class="forecast">
             {% for day in forecast %}
                <div class="day">
                    <strong>{{ day['date'] }}</strong><br>
                    {{ day['day']['condition']['text'] }}<br>
                    Max: {{ day['day']['maxtemp_c'] }}°C<br>
                    Min: {{ day['day']['mintemp_c'] }}°C
                </div>
                {% endfor %}
            </div>
            {% endif %}
        </div>
    </div>
    <marquee behavior="scroll" direction="left" class= "scroll-text">🌤 Welcome to GLOBAL WEATHER! Stay updated on the latest forecasts. 🌧</marquee>
    <footer class="site-footer">
   <div class="down-context">
        <div>
            <p class="copy">&copy; 2025 GLOBAL WEATHER | All rights reserved.</p>
        </div>
        <div class="bio">
            <p>By: Someshwar Sreeram</p>
            <p>Tools: HTML, CSS, Weather API, Flash Server</p>
        </div>
        <div class="logo-foot">
            <img class="logo" src ="https://res.cloudinary.com/dwkoy5wtd/image/upload/v1748721579/ChatGPT_Image_May_31_2025_at_05_49_34_AM_r7ilzn.png" alt="Logo"/>
        </div>
   </div>
</footer>

</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    temperature = None
    forecast = None
    location = None
    if request.method == 'POST':
        location = request.form['location']
        current_params = {
            'key': API_KEY,
            'q': location,
            'aqi': 'yes'
        }
        forecast_params = {
            'key': API_KEY,
            'q': location,
            'days': 5
        }
        current_response = requests.get(CURRENT_WEATHER_URL, params=current_params)
        forecast_response = requests.get(FORECAST_URL, params=forecast_params)

        if current_response.status_code == 200:
            data = current_response.json()
            temperature = data['current']['temp_c']
        else:
            temperature = 'Error: Could not fetch current data'

        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()
            forecast = forecast_data['forecast']['forecastday']

    return render_template_string(HTML_TEMPLATE, temperature=temperature, location=location, forecast=forecast)

if __name__ == '__main__':
    app.run(debug=True)
