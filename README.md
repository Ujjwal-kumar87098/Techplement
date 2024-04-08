# Techplement
Python Internship

Weather Checking Application

Task: Build a Weather Checking Application
Description:
Develop a command-line weather checking application using Python, with options-based control over the application behavior. Implement functionalities such as:

Checking weather by city name.
CRUD (Create, Read, Update, Delete) operations on a favorite list of cities.
Auto-refresh after 15-30 seconds.
Ensure proper error handling and data validation.

![image](https://github.com/Ujjwal-kumar87098/Techplement/assets/142151421/af52f238-f562-4efc-84fd-b93d77d7f46e)


Documentation of Commands

1. Check Weather by City Name
Command: weather -c <city_name>
Example: weather -c London
Description: Use this command to check the weather of a specific city.

2. Add City to Favorites
Command: weather -add <city_name>
Example: weather -add New York
Description: Add a city to your list of favorite cities.

3. Remove City from Favorites
Command: weather -remove <city_name>
Example: weather -remove Paris
Description: Remove a city from your list of favorite cities.

4. List Favorite Cities
Command: weather -list
Example: weather -list
Description: List all the cities saved as favorites.

5. Update Weather Data
Command: weather -update
Example: weather -update
Description: Manually update weather data.

6. Auto-Refresh
Command: weather -auto <interval>
Example: weather -auto 30
Description: Enable auto-refresh with a specified interval in seconds.
API
This application uses the WeatherAPI for fetching weather data.
