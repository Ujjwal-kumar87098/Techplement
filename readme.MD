# Command Line Weather Application

This is a simple command-line application written in Python for checking weather information using the WeatherAPI service. It allows users to perform various actions such as checking weather by city name, managing a list of favorite cities, and auto-refreshing weather data.

## Functionalities

### 1. Check Weather
   - Use the `check` action to fetch and display the current weather for a specific city.
   - Example: `python weather_app.py check --city London`

### 2. Add Favorite City
   - Use the `add` action to add a city to the list of favorite cities.
   - Example: `python weather_app.py add --favorite Paris`

### 3. Remove Favorite City
   - Use the `remove` action to remove a city from the list of favorite cities.
   - Example: `python weather_app.py remove --favorite Paris`

### 4. List Favorite Cities
   - Use the `list` action to display the list of favorite cities.
   - Example: `python weather_app.py list`

### 5. Auto-refresh Weather
   - Use the `refresh` action to continuously fetch and display weather data for a specific city at regular intervals.
   - Example: `python weather_app.py refresh --city NewYork --interval 30`

## Usage

1. **Installation**
   - Install Python if not already installed: [Python Installation Guide](https://www.python.org/downloads/)
   - Install required dependencies using pip:
     ```
     pip install requests python-dotenv
     ```

2. **Setup**
   - Obtain an API key from WeatherAPI: [WeatherAPI](https://www.weatherapi.com/)
   - Create a `.env` file in the same directory as the script and add your API key:
     ```
     API_KEY=your_api_key_here
     ```

3. **Running the Application**
   - Open a terminal or command prompt and navigate to the directory containing the script.
   - Run the script with appropriate command-line arguments to perform desired actions as described above.

## Dependencies
- `requests`: For making HTTP requests to the WeatherAPI service.
- `python-dotenv`: For loading environment variables from a .env file.

## Author
- Created by Ujjwal
