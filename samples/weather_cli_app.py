import requests

def get_weather(city, api_key="YOUR_API_KEY"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]
        print(f"Weather in {city}: {temp}°C, {desc}")
    else:
        print("City not found.")

# Example usage
get_weather("Kozhikode", "YOUR_API_KEY")
