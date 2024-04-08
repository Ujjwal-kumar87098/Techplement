import requests
from dotenv import load_dotenv
import sys
import time
import argparse
import os

load_dotenv()

city = sys.argv[1]

API_KEY = os.getenv("API_KEY")

BASE_URL =  "http://api.weatherapi.com/v1"

# Function to fetch weather data for a city
def get_weather(city):
    try:
        url = f"{BASE_URL}/current.json?key={API_KEY}&q={city}"
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for 4xx or 5xx status codes
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
    except KeyError:
        print("Invalid API response format.")
        return None

# Function to add a city to favorites list
def add_favorite(city):
    with open("favorites.txt", "a") as file:
        file.write(city + "\n")

# Function to remove a city from favorites list
def remove_favorite(city):
    try:
        with open("favorites.txt", "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.strip() != city:
                    file.write(line)
            file.truncate()
    except FileNotFoundError:
        print("Favorites list not found.")

# Function to list all favorite cities
def list_favorites():
    try:
        with open("favorites.txt", "r") as file:
            favorites = file.readlines()
            if favorites:
                for idx, city in enumerate(favorites, start=1):
                    print(f"{idx}. {city.strip()}")
            else:
                print("Favorites list is empty.")
    except FileNotFoundError:
        print("Favorites list not found.")

# Function to refresh weather data
def refresh_weather(city, interval):
    while True:
        weather_data = get_weather(city)
        if weather_data:
            print(f"Weather in {city}: {weather_data['current']['condition']['text']}, "
                  f"Temperature: {weather_data['current']['temp_c']}°C")
        time.sleep(interval)

def main():
    parser = argparse.ArgumentParser(description="Command Line Weather Application")
    parser.add_argument("action", choices=["check", "add", "remove", "list", "refresh"], help="Action to perform")
    parser.add_argument("--city", help="City name")
    parser.add_argument("--favorite", help="Favorite city name")
    parser.add_argument("--interval", type=int, default=15, help="Interval for auto-refresh in seconds")
    args = parser.parse_args()

    if args.action == "check":
        if args.city:
            weather_data = get_weather(args.city)
            if weather_data:
                print(f"Weather in {args.city}: {weather_data['current']['condition']['text']}, "
                      f"Temperature: {weather_data['current']['temp_c']}°C")
        else:
            print("Please provide a city name.")
    elif args.action == "add":
        if args.favorite:
            add_favorite(args.favorite)
            print(f"{args.favorite} added to favorites.")
        else:
            print("Please provide a city name to add to favorites.")
    elif args.action == "remove":
        if args.favorite:
            remove_favorite(args.favorite)
            print(f"{args.favorite} removed from favorites.")
        else:
            print("Please provide a city name to remove from favorites.")
    elif args.action == "list":
        list_favorites()
    elif args.action == "refresh":
        if args.city:
            refresh_weather(args.city, args.interval)
        else:
            print("Please provide a city name to refresh weather.")

if __name__ == "__main__":
    main()
