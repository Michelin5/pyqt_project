# Подключаю все необходимые библиотеки

import requests
from pprint import pprint

app_id = '07fd9e87806a3b778c76e0a21639f307'  # это специальный ключ, который вадают при регистрации на сайте
# openweathermap, который нужен для получения данных о погоде с сайта

city = input()

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric'.format(
    city, app_id)

data = requests.get(url).json()  # получаем данные с сайта и преобразовываем их в читаемый формат json

# Записываем в переменные данные о погоде

temp = str(data['main']['temp']) + ' °С'  # актуальная температура
vlazhnost = str(data['main']['humidity']) + ' %'  # влажность
davlenie = str(data['main']['pressure'] / (4 / 3)) + ' мм.рт.ст.'  # давление
tempmax = str(data['main']['temp_max']) + ' °С'  # максимальная температура
tempmin = str(data['main']['temp_min']) + ' °С'  # минимальная температура
