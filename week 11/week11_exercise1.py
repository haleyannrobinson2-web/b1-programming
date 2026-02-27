# EU Capitals Weather
# Data Collection

import requests
import json
import time

# List of EU capitals (from lab sheet)
eu_capitals = [
    {"city": "Vienna", "country": "Austria", "lat": 48.2082, "lon": 16.3738},
    {"city": "Brussels", "country": "Belgium", "lat": 50.8503, "lon": 4.3517},
    {"city": "Sofia", "country": "Bulgaria", "lat": 42.6977, "lon": 23.3219},
    {"city": "Zagreb", "country": "Croatia", "lat": 45.8150, "lon": 15.9819},
    {"city": "Nicosia", "country": "Cyprus", "lat": 35.1856, "lon": 33.3823},
    {"city": "Prague", "country": "Czechia", "lat": 50.0755, "lon": 14.4378},
    {"city": "Copenhagen", "country": "Denmark", "lat": 55.6761, "lon": 12.5683},
    {"city": "Tallinn", "country": "Estonia", "lat": 59.4370, "lon": 24.7536},
    {"city": "Helsinki", "country": "Finland", "lat": 60.1695, "lon": 24.9354},
    {"city": "Paris", "country": "France", "lat": 48.8566, "lon": 2.3522},
    {"city": "Berlin", "country": "Germany", "lat": 52.5200, "lon": 13.4050},
    {"city": "Athens", "country": "Greece", "lat": 37.9838, "lon": 23.7275},
    {"city": "Budapest", "country": "Hungary", "lat": 47.4979, "lon": 19.0402},
    {"city": "Dublin", "country": "Ireland", "lat": 53.3498, "lon": -6.2603},
    {"city": "Rome", "country": "Italy", "lat": 41.9028, "lon": 12.4964},
    {"city": "Riga", "country": "Latvia", "lat": 56.9496, "lon": 24.1052},
    {"city": "Vilnius", "country": "Lithuania", "lat": 54.6872, "lon": 25.2797},
    {"city": "Luxembourg", "country": "Luxembourg", "lat": 49.6116, "lon": 6.1319},
    {"city": "Valletta", "country": "Malta", "lat": 35.8989, "lon": 14.5146},
    {"city": "Amsterdam", "country": "Netherlands", "lat": 52.3676, "lon": 4.9041},
    {"city": "Warsaw", "country": "Poland", "lat": 52.2297, "lon": 21.0122},
    {"city": "Lisbon", "country": "Portugal", "lat": 38.7223, "lon": -9.1393},
    {"city": "Bucharest", "country": "Romania", "lat": 44.4268, "lon": 26.1025},
    {"city": "Bratislava", "country": "Slovakia", "lat": 48.1486, "lon": 17.1077},
    {"city": "Ljubljana", "country": "Slovenia", "lat": 46.0569, "lon": 14.5058},
    {"city": "Madrid", "country": "Spain", "lat": 40.4168, "lon": -3.7038},
    {"city": "Stockholm", "country": "Sweden", "lat": 59.3293, "lon": 18.0686}
]

# This dictionary will store ALL results
all_weather_data = {}

# Loop through each capital
for capital in eu_capitals:
    city = capital["city"]
    country = capital["country"]
    lat = capital["lat"]
    lon = capital["lon"]

    print("Getting data for:", city)

    # API URL (current weather + hourly forecast for today)
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&current_weather=true"
        f"&hourly=temperature_2m,precipitation_probability,weathercode"
        f"&forecast_days=1"
        f"&timezone=auto"
    )

    try:
        response = requests.get(url, timeout=10)

        # Check if request worked
        if response.status_code == 200:
            data = response.json()

            # Extract current weather
            current = data.get("current_weather", {})

            # Extract hourly data
            hourly = data.get("hourly", {})

            hourly_forecast = []

            times = hourly.get("time", [])
            temps = hourly.get("temperature_2m", [])
            precipitation = hourly.get("precipitation_probability", [])
            codes = hourly.get("weathercode", [])

            # Combine hourly data into list of dictionaries
            for i in range(len(times)):
                hourly_forecast.append({
                    "time": times[i],
                    "temperature": temps[i] if i < len(temps) else None,
                    "precipitation_probability": precipitation[i] if i < len(precipitation) else None,
                    "weathercode": codes[i] if i < len(codes) else None
                })

            # Save structured data
            all_weather_data[city] = {
                "country": country,
                "coordinates": {
                    "latitude": lat,
                    "longitude": lon
                },
                "current_weather": current,
                "hourly_forecast": hourly_forecast
            }

        else:
            print("Error for", city, "- Status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Network error for", city, ":", e)

    except Exception as e:
        print("Unexpected error for", city, ":", e)

    # Delay to respect API rate limits
    time.sleep(1)

# Save to JSON file
with open("eu_weather_data.json", "w") as file:
    json.dump(all_weather_data, file, indent=4)

print("Finished! Data saved to eu_weather_data.json")