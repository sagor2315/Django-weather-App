from django.shortcuts import render
import json
import requests


def weather_api(city):
    API_key = '8051b0f1410ab0f1cf8ee8de5f25428a'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric'

    r = requests.get(url)
    if r.status_code == 200:
        data = json.loads(r.text)

        results = {}
        temp = data.get('main').get('temp')
        weather = data.get('weather')[0].get('description')
        city_name = data.get('name')
        country = data.get('sys').get('country')
        timezone = data.get('timezone')

        results['country'] = country
        results['city_name'] = city_name
        results['timezone'] = timezone
        results['weather'] = weather
        results['temp'] = temp
    else:
        results = {'error': f'Failed to retrieve weather data for {city}'}

    return results


def home_view(request):
    if request.method == "GET" and 'City' in request.GET:
        city = request.GET.get('City')
        results = weather_api(city)
        context = {'results': results}
    else:
        context = {}

    return render(request, 'home.html', context)

