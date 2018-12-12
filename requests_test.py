import requests
from pprint import pprint

app_id = '07fd9e87806a3b778c76e0a21639f307'

city = input()

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric'.format(
    city, app_id)

data = requests.get(url).json()

temp = str(data['main']['temp']) + ' °С'
vlazhnost = str(data['main']['humidity']) + ' %'
davlenie = str(data['main']['pressure'] / (4/3)) + ' мм.рт.ст.'
tempmax = str(data['main']['temp_max']) + ' °С'
tempmin = str(data['main']['temp_min']) + ' °С'


