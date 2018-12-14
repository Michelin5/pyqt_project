# Подключаю все необходимые библиотеки
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QLabel, QLineEdit
from PyQt5 import QtGui, QtCore
import requests
from pprint import pprint
from PyQt5.QtCore import Qt

app_id = '07fd9e87806a3b778c76e0a21639f307'  # это специальный ключ, который вадают при регистрации на сайте


# openweathermap, который нужен для получения данных о погоде с сайта

# city = input()

# url = 'https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric'.format(
# city, app_id)

# data1 = requests.get(url1).json()  # получаем данные с сайта и преобразовываем их в читаемый формат json

# Записываем в переменные данные о погоде

# temp = str(data['main']['temp']) + ' °С'  # актуальная температура
# vlazhnost = str(data['main']['humidity']) + ' %'  # влажность
# davlenie = str(data['main']['pressure'] / (4 / 3)) + ' мм.рт.ст.'  # давление
# tempmax = str(data['main']['temp_max']) + ' °С'  # максимальная температура
# tempmin = str(data['main']['temp_min']) + ' °С'  # минимальная температура


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        color = 'blue'  # Задаю изначальный цвет каждого параметра
        startlabel = 'Введите город'  # Задаю изначальную надпись каждого параметра
        x, y = 100, 13

        # Задаю фон

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.lightGray)
        self.setPalette(p)

        # Далее я создаю виджеты

        self.label_theme = QLabel(self)
        self.label_theme.setText('Выберите тему:')
        self.label_theme.move(400, 210)

        self.buttongray = QPushButton('Серая', self)
        self.buttongray.move(400, 235)
        self.buttongray.clicked.connect(self.changetheme)

        self.buttongreen = QPushButton('Белая', self)
        self.buttongreen.move(400, 270)
        self.buttongreen.clicked.connect(self.changetheme)

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Погода')

        self.btn = QPushButton('Показать погоду', self)
        self.btn.move(185, 350)
        self.btn.resize(120, 50)
        self.btn.clicked.connect(self.weather)

        self.btn.setStyleSheet('QPushButton:hover { background-color: lightGray }'
                               'QPushButton:!hover { background-color: white }')

        self.city_input = QLineEdit(self)
        self.city_input.move(190, 50)
        self.city_input.resize(100, 30)

        self.label = QLabel(self)
        self.label.setText("Введите название города на английском:")
        self.label.move(135, 25)

        self.label_temp = QLabel(self)
        self.label_temp.setText("Температура:")
        self.label_temp.move(30, 120)

        self.temp = QLabel(self)
        self.temp.move(110, 120)
        self.temp.resize(x, y)
        self.temp.setText(startlabel)
        palet = self.temp.palette()
        palet.setColor(QtGui.QPalette.WindowText, QtGui.QColor(color))
        self.temp.setPalette(palet)

        self.label_humidity = QLabel(self)
        self.label_humidity.setText("Влажность:")
        self.label_humidity.move(30, 160)

        self.humidity = QLabel(self)
        self.humidity.move(110, 160)
        self.humidity.setText(startlabel)
        self.humidity.resize(x, y)
        palet = self.humidity.palette()
        palet.setColor(QtGui.QPalette.WindowText, QtGui.QColor(color))
        self.humidity.setPalette(palet)

        self.label_pressure = QLabel(self)
        self.label_pressure.setText('Давление:')
        self.label_pressure.move(30, 200)

        self.pressure = QLabel(self)
        self.pressure.move(110, 200)
        self.pressure.setText(startlabel)
        self.pressure.resize(x, y)
        palet = self.pressure.palette()
        palet.setColor(QtGui.QPalette.WindowText, QtGui.QColor(color))
        self.pressure.setPalette(palet)

        self.label_tempmin = QLabel(self)
        self.label_tempmin.setText('Мин. темп:')
        self.label_tempmin.move(30, 240)

        self.tempmin = QLabel(self)
        self.tempmin.move(110, 240)
        self.tempmin.setText(startlabel)
        self.tempmin.resize(x, y)
        palet = self.tempmin.palette()
        palet.setColor(QtGui.QPalette.WindowText, QtGui.QColor(color))
        self.tempmin.setPalette(palet)

        self.label_tempmax = QLabel(self)
        self.label_tempmax.setText('Макс. темп:')
        self.label_tempmax.move(30, 280)

        self.tempmax = QLabel(self)
        self.tempmax.move(110, 280)
        self.tempmax.setText(startlabel)
        self.tempmax.resize(x, y)
        palet = self.tempmax.palette()
        palet.setColor(QtGui.QPalette.WindowText, QtGui.QColor(color))
        self.tempmax.setPalette(palet)

        self.label_error = QLabel(self)
        self.label_error.setText('Статус ошибок:')
        self.label_error.move(280, 120)

        self.error = QLabel(self)
        self.error.setText('Ошибок не обнаружено.')
        self.error.move(370, 120)
        paleterror = self.error.palette()
        paleterror.setColor(QtGui.QPalette.WindowText, QtGui.QColor('green'))
        self.error.setPalette(paleterror)

    def changetheme(self):
        if self.sender().text() == 'Серая':
            self.setAutoFillBackground(True)
            p = self.palette()
            p.setColor(self.backgroundRole(), Qt.lightGray)
            self.setPalette(p)
        elif self.sender().text() == 'Белая':
            self.setAutoFillBackground(True)
            p = self.palette()
            p.setColor(self.backgroundRole(), Qt.white)
            self.setPalette(p)

    def weather(self):
        try:
            city = self.city_input.text()
            url = 'https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric'.format(
                city, app_id)
            data = requests.get(url).json()
            temp = str(data['main']['temp']) + ' °С'  # актуальная температура
            vlazhnost = str(data['main']['humidity']) + ' %'  # влажность
            davlenie = str(data['main']['pressure'] / (4 / 3)) + ' мм.рт.ст.'  # давление
            tempmax = str(data['main']['temp_max']) + ' °С'  # максимальная температура
            tempmin = str(data['main']['temp_min']) + ' °С'  # минимальная температура
            wind = str(data['wind']['speed']) + ' м/с'
            self.temp.setText(temp)
            self.humidity.setText(vlazhnost)
            self.pressure.setText(davlenie)
            self.tempmin.setText(tempmin)
            self.tempmax.setText(tempmax)
            paleterror = self.error.palette()
            paleterror.setColor(QtGui.QPalette.WindowText, QtGui.QColor('green'))
            self.error.setPalette(paleterror)
            self.error.setText('Ошибок не обнаружено.')


        except Exception:
            errorcolor = 'red'
            errorlabel = "Город не найден"
            self.error.setText('Проверьте город.')
            paleterror = self.error.palette()
            paleterror.setColor(QtGui.QPalette.WindowText, QtGui.QColor(errorcolor))
            self.error.setPalette(paleterror)
            self.temp.setText(errorlabel)
            self.humidity.setText(errorlabel)
            self.pressure.setText(errorlabel)
            self.tempmin.setText(errorlabel)
            self.tempmax.setText(errorlabel)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
