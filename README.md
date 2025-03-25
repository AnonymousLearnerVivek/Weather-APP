# Weather-APP

# Weather App

## Description
The Weather App is a simple Python application that fetches real-time weather data using the OpenWeatherMap API. Users can enter the name of a city, and the app will retrieve the current weather conditions, including temperature, humidity, and weather description.

## Features
- Fetches real-time weather data from OpenWeatherMap API
- Displays temperature, humidity, and weather conditions
- Handles API errors such as invalid API keys and rate limits
- User-friendly command-line interface

## Requirements
- Python 3.x
- `requests` library

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/AnonymousLearnerVivek/Weather-APP
   cd weather-app
   ```
2. Install dependencies:
   ```sh
   pip install requests
   ```
3. Get an API key from [OpenWeatherMap](https://openweathermap.org/api) and replace `API_key` in the script.

## Usage
1. Run the script:
   ```sh
   python weather_app.py
   ```
2. Enter the name of the city when prompted.
3. View the weather details displayed on the screen.

## Error Handling
- **Invalid API Key (401):** Ensure you have entered a valid API key.
- **API Rate Limit Exceeded (429):** Wait and try again later.
- **Other Errors:** The app will display the response code and error message.

## Example Output
```
Enter the name of the city: London
Success:
Weather is  clear sky
Current temperature is  15°C
Current temperature feels like is  13°C
Humidity is  60%
```

## License
This project is open-source and available under the MIT License.

## Author
Vivek Surana

## Acknowledgments
- [OpenWeatherMap API](https://openweathermap.org/api)

