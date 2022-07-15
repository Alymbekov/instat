import requests
from typing import List


def get_geo() -> List[dict]:
    urls = ['http://api.openweathermap.org/geo/1.0/direct?q=London&limit=1&appid=8a4ddf3b661749d7d19b9db8fc17c902',
            'http://api.openweathermap.org/geo/1.0/direct?q=Warsaw&limit=1&appid=8a4ddf3b661749d7d19b9db8fc17c902',
            'http://api.openweathermap.org/geo/1.0/direct?q=Moscow&limit=1&appid=8a4ddf3b661749d7d19b9db8fc17c902']

    cities = []
    geo_positions = []
    for url in urls:
        cities.append(requests.get(url).json())
    
    for city in cities:
        lat = city[0].get('lat')
        lon = city[0].get('lon')
        dict_ = {'lat': lat, 'lon': lon}
        geo_positions.append(dict_)
    return geo_positions


def generate_new_urls() -> List[str]:
    old_urls = [
        'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=8a4ddf3b661749d7d19b9db8fc17c902',
        'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=8a4ddf3b661749d7d19b9db8fc17c902',
        'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=8a4ddf3b661749d7d19b9db8fc17c902']
    geo_locations = get_geo()
    new_urls = []
    for index, url in enumerate(old_urls):
        lat = geo_locations[index]['lat']
        lon = geo_locations[index]['lon']
        new_urls.append(url.format(lat=lat, lon=lon))
    return new_urls
