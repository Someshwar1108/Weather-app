
# 🌦 Weather Forecast App

The **Weather Forecast App** is a web-based application built using modern frontend technologies (HTML, CSS, JavaScript) that connects to public weather APIs such as OpenWeatherMap to deliver real-time weather updates. It allows users to search for any city or ZIP code and provides key weather details, including current temperature, conditions, humidity, wind speed, and a 5-day forecast. Designed with a focus on clean UI and intuitive interaction, this project demonstrates how to integrate third-party APIs into a responsive frontend application, making it an excellent example of practical API consumption and user-centered web design.

---

### 🌟 Features

* **Real-time Weather Data**
  Get current temperature, weather conditions, humidity, and wind speed for any location.

* **5-Day Forecast**
  View upcoming weather predictions with intuitive weather icons (e.g., sunny, rainy, cloudy).

* **City Search Bar**
  Easily search by city name or ZIP code to retrieve local weather.

* **Responsive UI**
  Designed for seamless use on both desktop and mobile browsers.

* **Error Handling**
  Handles cases like invalid city names or API errors gracefully, showing user-friendly messages.

---

### 📁 Project Files

* **`index.html` / `App.js`**
  Core frontend structure and layout, including the search bar and weather display components.

* **`style.css`**
  Contains all styles for the app, ensuring a clean and responsive design.

* **`README.md`**
  Documentation providing an overview of the project’s purpose, features, and setup instructions.

---

### 🛠 Design Choices

* **API Integration**
  The decision to use the OpenWeatherMap API (or similar) allows for robust and reliable access to global weather data, enabling a wide range of location searches.

* **Modular Frontend**
  The app’s design separates concerns, keeping API logic, UI components, and styling distinct. This improves maintainability and makes it easier to scale features (e.g., adding air quality or UV index).

* **Error Handling**
  Incorporating error checks ensures that users receive clear feedback when an invalid city is entered or if there’s a network/API issue, enhancing the user experience.

* **Scalable Design**
  The project is built in a way that can be extended later, for example, to include geolocation-based weather, unit toggles (°C/°F), or even backend features using Node.js or Flask.

