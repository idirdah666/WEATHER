import argparse
import imp
import json
import argparse
from configparser import ConfigParser
from urllib import parse, request, error

BASE_WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"

def _get_api_key_ ():
    """Get the API key from the config file."""
    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]

def read_user_cli_args():
    """Read the user's command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--city', help='the city to get the weather for')
    parser.add_argument('--units', help='the units to display the temperature in')
    return parser.parse_args()



def get_weather_data(config):
    """Get the weather data from the OpenWeatherMap API."""
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': config['city'],
        'units': config['units'],
        'appid': config['api_key'],
    }
    url += '?' + parse.urlencode(params)
    response = request.urlopen(url)
    return json.loads(response.read().decode('utf-8'))

if __name__ == '__main__':
    args = read_user_cli_args()
    config = {
        'city': args.city,
        'units': args.units,
        'api_key': _get_api_key_(),
    }
    weather_data = get_weather_data(config)
    print(weather_data)





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('config_file')
    args = parser.parse_args()
    config = ConfigParser()
    config.read(args.config_file)
    weather_data = get_weather_data(config['openweathermap'])
    print(weather_data)


print ("Hello world!")
