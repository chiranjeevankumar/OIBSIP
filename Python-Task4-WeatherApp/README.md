# Basic Weather App

## Description
A Python command-line app that fetches current weather for a city.

## Features
- City name input and empty-input validation
- Current temperature in Celsius and Fahrenheit
- Humidity percentage
- Weather condition description
- Wind speed in km/h
- Handles unknown cities, network errors, and timeouts

## Technologies
- Python 3
- requests
- Open-Meteo geocoding and forecast APIs

## Installation
Install the required package:

```bash
pip install requests
```

## Run
```bash
python weather_app.py
```

## Privacy
The entered city name is sent to Open-Meteo to find its coordinates.
Those coordinates are used to request weather data. No API key is required.
