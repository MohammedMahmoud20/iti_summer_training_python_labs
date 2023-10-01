import requests

api_key = '0bc4c405a5364b0697e105547232509'

def get_current_temperature(city,api_key):
    base_url = 'https://api.weatherapi.com/v1/current.json'
    response = requests.get(base_url, params={'key': api_key, 'q': city})
    if response.status_code == 200:
        data = response.json()
        current_temp_c = data['current']['temp_c']
        current_temp_f = data['current']['temp_f']
        return f"The current temperature in {city} is {current_temp_c}°C ({current_temp_f}°F)."
    else:
        return f"Unable to retrieve the current temperature for {city}. Error: {response.status_code}"


def get_temperature_after(api_key,city, days, hour=None):
    base_url = 'https://api.weatherapi.com/v1/forecast.json'
    response = requests.get(base_url, params={'key': api_key, 'q': city, 'days': days})
    if response.status_code == 200:
        data = response.json()
        if 'forecast' in data and 'forecastday' in data['forecast'] and len(data['forecast']['forecastday']) > days:
            if hour and 'hour' in data['forecast']['forecastday'][days] and len(data['forecast']['forecastday'][days]['hour']) > hour:
                forecast_temp_c = data['forecast']['forecastday'][days]['hour'][hour]['temp_c']
                forecast_temp_f = data['forecast']['forecastday'][days]['hour'][hour]['temp_f']
                return f"The temperature in {city} after {days} days at {hour}:00 will be {forecast_temp_c}°C ({forecast_temp_f}°F)."
            elif 'day' in data['forecast']['forecastday'][days]:
                forecast_temp_c = data['forecast']['forecastday'][days]['day']['avgtemp_c']
                forecast_temp_f = data['forecast']['forecastday'][days]['day']['avgtemp_f']
                return f"The average temperature in {city} after {days} days will be {forecast_temp_c}°C ({forecast_temp_f}°F)."
            else:
                return f"No temperature data available for the specified hour or day."
        else:
            return f"No temperature data available for the specified number of days."
    else:
        return f"Unable to retrieve the temperature forecast for {city}. Error: {response.status_code}"


def get_lat_and_long(api_key,city):
    base_url = 'https://api.weatherapi.com/v1/current.json'
    response = requests.get(base_url, params={'key': api_key, 'q': city})
    if response.status_code == 200:
        data = response.json()
        latitude = data['location']['lat']
        longitude = data['location']['lon']
        return f"The coordinates of {city} are Latitude: {latitude}, Longitude: {longitude}."
    else:
        return f"Unable to retrieve the coordinates for {city}. Error: {response.status_code}"





city = 'EGYPT'
current_temperature = get_current_temperature(city,api_key)
print(current_temperature)


days = 1
hour = 12
temperature_after = get_temperature_after(api_key,city, days, hour)
print(temperature_after)

coordinates = get_lat_and_long(api_key,city)
print(coordinates)
