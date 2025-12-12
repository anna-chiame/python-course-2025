import requests

API_KEY = "25c14572e7c5849405976ef258b0df63"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str) -> dict:
    """
    Sends a request to OpenWeatherMap API and returns weather data.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",   # Celsius
        "lang": "en"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def main():
    city = input("Enter city name: ")

    try:
        data = get_weather(city)

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("\nCurrent weather:")
        print(f"City: {city}")
        print(f"Temperature: {temperature} °C")
        print(f"Feels like: {feels_like} °C")
        print(f"Humidity: {humidity}%")
        print(f"Wind speed: {wind_speed} m/s")
        print(f"Description: {description}")


    except requests.exceptions.HTTPError as e:

        print("HTTP error:", e)

        print("Response:", e.response.text)


if __name__ == "__main__":
    main()
