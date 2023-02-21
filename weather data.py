import requests
from bs4 import BeautifulSoup as bs
import json
from pprint import pprint

# city_name = input('enter your city name: ')
# API_key = '8051b0f1410ab0f1cf8ee8de5f25428a'
# url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=imperial'
# r = requests.get(url)
# data = json.loads(r.text)
#
# results = {}
# temp = data.get('main').get('temp')
# weather = data.get('weather')[0].get('description')
# city_name = data.get('name')
# country = data.get('sys').get('country')
# timezone = data.get('timezone')
#
# results['temp'] = temp
# results['weather'] = weather
# results['city_name'] = city_name
# results['country'] = country
# results['timezone'] = timezone
#
# pprint(results)

def weather_api(city):
    api_key = '8051b0f1410ab0f1cf8ee8de5f25428a'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = json.loads(response.text)
    results = {}
    results['lon'] = data['coord']['lon']
    results['lat'] = data['coord']['lat']
    results['name'] =data['name']
    results['temp'] =data['main']['temp']
    results['humidity'] =data['main']['humidity']
    return results

print(weather_api('dhaka'))