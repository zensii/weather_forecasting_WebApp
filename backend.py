import requests

api_key = '7b4399da7be67faa3abd9e590c87a3ea'


def get_location(city_name):

    query = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}'
    response = requests.get(query)
    response = response.json()
    lat = response[0]['lat']
    lon = response[0]['lon']
    return lat, lon


def get_data(lat, lon, days):

    query = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&cnt={days * 8}&appid={api_key}&units=metric'
    response = requests.get(query)
    data = response.json()

    return data


def get_current(location):
     query = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
     response = requests.get(query)
     current = response.json()

     return current


if __name__ == '__main__':
    lat, lon = get_location('Anchorage')
    data = get_data(lat, lon, days=3)
    current = get_current('Anchorage')