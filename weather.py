import requests
from dotenv import load_dotenv
import os
from pprint import pprint

# Load environment variables
load_dotenv()

def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')

    # Prompt user for city name
    city = input("\nPlease Enter a city name:\n").strip()

    # Get the API key from environment variables
    api_key = os.getenv("API_KEY")  # Use API_KEY without spaces in the .env file

    if not api_key:
        print("Error: API key is missing. Check your .env file.")
        return

    # Construct the request URL
    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={api_key}&q={city}&units=metric'

    # Print URL for debugging (optional)
    print(f"\nRequest URL: {request_url}\n")

    # Make the API request
    response = requests.get(request_url)
    weather_data = response.json()

    # Check if the API call was successful
    if weather_data.get("cod") == 200:
        # Display weather data
        print(f'\nCurrent weather for {weather_data["name"]}:')
        print(f'Temperature: {weather_data["main"]["temp"]:.1f}°C')
        print(f'Weather: {weather_data["weather"][0]["description"].capitalize()}')
    else:
        # Handle errors (e.g., invalid city or API key)
        print(f"Error: {weather_data.get('message', 'Unknown error')}")

# Call the function
get_current_weather()
