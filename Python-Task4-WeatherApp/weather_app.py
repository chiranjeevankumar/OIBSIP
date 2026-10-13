import requests

def get_weather():
    print("=== Basic Weather App ===")
    city = input("Enter city name: ").strip()

    if not city:
        print("Error: City name cannot be empty.")
        return

    try:
        geo_response = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city, "count": 1, "language": "en"},
            timeout=10
        )
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if not geo_data.get("results"):
            print("Error: City not found. Please try another city.")
            return

        place = geo_data["results"][0]
        latitude = place["latitude"]
        longitude = place["longitude"]

        weather_response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,relative_humidity_2m,"
                    "weather_code,wind_speed_10m"
                ),
                "temperature_unit": "celsius",
                "wind_speed_unit": "kmh"
            },
            timeout=10
        )
        weather_response.raise_for_status()
        current = weather_response.json()["current"]

        temp_c = current["temperature_2m"]
        temp_f = temp_c * 9 / 5 + 32

        descriptions = {
            0: "Clear sky", 1: "Mainly clear",
            2: "Partly cloudy", 3: "Overcast",
            45: "Fog", 48: "Depositing rime fog",
            51: "Light drizzle", 53: "Moderate drizzle",
            55: "Dense drizzle", 61: "Slight rain",
            63: "Moderate rain", 65: "Heavy rain",
            71: "Slight snow", 73: "Moderate snow",
            75: "Heavy snow", 80: "Rain showers",
            81: "Moderate rain showers", 82: "Heavy rain showers",
            95: "Thunderstorm"
        }

        code = current["weather_code"]
        condition = descriptions.get(code, "Other weather conditions")

        print("\n--- Current Weather ---")
        print(f"Location: {place['name']}, {place.get('country', '')}")
        print(f"Temperature: {temp_c} °C")
        print(f"Temperature: {temp_f:.1f} °F")
        print(f"Humidity: {current['relative_humidity_2m']}%")
        print(f"Condition: {condition}")
        print(f"Wind speed: {current['wind_speed_10m']} km/h")

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")
    except requests.exceptions.RequestException:
        print("Error: Could not connect to the weather service.")
    except (KeyError, ValueError):
        print("Error: Could not read the weather data.")


if __name__ == "__main__":
    get_weather()
