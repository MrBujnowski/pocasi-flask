import requests

def fetch_weather_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    response = requests.get(url)
    data = response.json()
    return data

def display_temperature(data):
    current_temp = data.get('current', {}).get('temperature_2m')
    hourly_temps = data.get('hourly', {}).get('temperature_2m', [])
    
    print(f"Current Temperature: {current_temp}°C")
    print("Hourly Temperatures:")
    for temp in hourly_temps:
        print(f"{temp}°C")

if __name__ == "__main__":
    weather_data = fetch_weather_data()
    display_temperature(weather_data)