# Импортируем нужные модули.
from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox


# Функция проверки поля ввода координат. Разрешен тип float.
def validate_float(new_value):
    if new_value == "":
        return True  # разрешаем пустое поле

    try:
        float(new_value)
        return True
    except ValueError:
        return False


# Функция запроса погоды
def getweather(params_api):
    # Получаем ответ сервиса по запросу
    response = requests.get(url, params=params_api, headers={'X-Yandex-API-Key': api_key})
    # Проверяем статус ответа сервера (200 - ОК, 403 - Forbidden (Доступ запрещен), 404 - Page not found (страница ненайдена))
    if response.status_code == 200:
        # Преобразуем ответ в JSON-формат
        data = response.json()

        # Выводим в тесте данные о текущей погоде и заполняем список final полученными значениями погоды из json формата
        # print (str(f'Дата : {data["now_dt"]}'))

        print(f'Температура воздуха: {data["fact"]["temp"]} °C')
        temperature = data["fact"]["temp"]

        print(f'Ощущается как: {data["fact"]["feels_like"]} °C')
        temperature_feel = data["fact"]["feels_like"]

        print(f'Скорость ветра: {data["fact"]["wind_speed"]} м/с')
        wind_speed = data["fact"]["wind_speed"]

        print(f'Давление: {data["fact"]["pressure_mm"]} мм рт. ст.')
        pressure = data["fact"]["pressure_mm"]

        print(f'Влажность: {data["fact"]["humidity"]} %')
        humidity = data["fact"]["humidity"]

        print(f'Погодное описание: {data["fact"]["condition"]}')
        condition = data["fact"]["condition"]

        print(f'Время года: {data["fact"]["season"]}')
        season = data["fact"]["season"]

        final = [temperature, temperature_feel, wind_speed, pressure, humidity, condition, season]

        return final
    else:
        # Выводим код ошибки
        print(f'Ошибка: {response.status_code}')
        return None


# Функция определения параметров запроса и вызов функции getweather, заполнения виджетов полученными значениями погоды,
# также заполняет виджеты предупреждений по условиям погоды.
def search():
    # Задаем параметры запроса
    params = {'lat': city_entry_lat.get(),
              'lon': city_entry_lon.get(),
              'lang': 'ru_RU',
              }
    # Делаем запрос к сервису с параметрами запроса
    weather = getweather(params_api=params)

    if weather:
        location_lbl['text'] = 'Расположение - Широта {} , Долгота {}'.format(city_entry_lat.get(),
                                                                              city_entry_lon.get())
        temperature_label['text'] = 'Температура: ' + str(weather[0]) + ' С'
        if weather[0] < -15:
            temperature_alarm_label[
                'text'] = 'Внимание!!! Температура ниже критического значения -15 С. В ближайшее время в данной местности необходимо проверить изношенные теплотрассы на предмет аварий.'
        temperature_feel_label['text'] = 'Температура ощущается как: ' + str(weather[1]) + ' C'
        wind_speed_label['text'] = 'Скорость ветра: ' + str(weather[2]) + 'м/с'
        if weather[2] > 15:
            wind_alarm_label[
                'text'] = 'Внимание!!! Скорость ветра больше 15 м/с. В ближайшее время в данной местности необходимо проверить линии электропередач на предмет аварий!!!'
        pressure_label['text'] = 'Давление: ' + str(weather[3]) + ' мм. рт. ст.'
        humidity_label['text'] = 'Влажность: ' + str(weather[4]) + ' %'
        condition_label['text'] = 'Состояние погоды: ' + weather[5]
        season_label['text'] = 'Время года: ' + weather[6]
    else:
        messagebox.showerror('Error', 'Не могу найти погоду по координатам {}, {}.'.format(city_entry_lat.get(),
                                                                                           city_entry_lon.get()))


# Функция для открытия нового окна
def Kuzbas():
    new_window = Toplevel(app)
    new_window.title("Координаты городов Кузбасса")
    new_window.geometry("550x800+700+200")
    new_window.update_idletasks()
    Label(new_window, text="1. Анжеро-Судженск: Широта-56.081, Долгота-86.0285", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="2. Бачатский: Широта-54.2927, Долгота-86.1285", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="3. Белово: Широта-54.4165, Долгота-86.2976", font=("Times New Roman", 15)).pack(anchor="w")
    Label(new_window, text="4. Берёзовский: Широта-55.6, Долгота-86.2", font=("Times New Roman", 15)).pack(anchor="w")
    Label(new_window, text="5. Грамотеино: Широта-54.5368, Долгота-86.3839", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="6. Гурьевск: Широта-54.2833, Долгота-85.9333", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="7. Инской: Широта-54.4297, Долгота-86.44", font=("Times New Roman", 15)).pack(anchor="w")
    Label(new_window, text="8. Калтан: Широта-53.5347, Долгота-87.2457", font=("Times New Roman", 15)).pack(anchor="w")
    Label(new_window, text="9. Кедровка: Широта-55.5214, Долгота-86.0951", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="10. Кемерово: Широта-55.3333, Долгота-86.0833", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="11. Киселёвск: Широта-53.99, Долгота-86.6621", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="12. Краснобродский: Широта-54.1581, Долгота-86.4486", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="13. Ленинск-Кузнецкий: Широта-54.6567, Долгота-86.1737", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="14. Мариинск: Широта-56.2139, Долгота-87.7472", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="15. Междуреченск: Широта-53.6942, Долгота-53.6942", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="16. Мыски: Широта-53.709, Долгота-87.8014", font=("Times New Roman", 15)).pack(anchor="w")
    Label(new_window, text="17. Новокузнецк: Широта-53.7557, Долгота-87.1099", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="18. Осинники: Широта-53.6239, Долгота-87.3598", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="19. Полысаево: Широта-54.6012, Долгота-86.2459", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="20. Прокопьевск: Широта-53.9059, Долгота-86.719", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="21. Промышленная: Широта-54.9159, Долгота-85.6385", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="22. Тайга: Широта-56.064, Долгота-85.6224", font=("Times New Roman", 15)).pack(anchor="w")
    Label(new_window, text="23. Таштагол: Широта-52.7657, Долгота-87.8894", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="24. Топки: Широта-55.2769, Долгота-85.6163", font=("Times New Roman", 15)).pack(anchor="w")
    Label(new_window, text="25. Тяжинский: Широта-56.1161, Долгота-88.5228", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="26. Шерегеш: Широта-52.9209, Долгота-87.9869", font=("Times New Roman", 15)).pack(
        anchor="w")
    Label(new_window, text="27. Яшкино: Широта-55.8736, Долгота-85.4265", font=("Times New Roman", 15)).pack(anchor="w")
    Label(new_window, text="28. Яя: Широта-56.206, Долгота-86.44", font=("Times New Roman", 15)).pack(anchor="w")
    Label(new_window, text="Северный полюс: Широта-90, Долгота-0", font=("Times New Roman", 15)).pack(anchor="nw")


# Парсим конфигурационный файл, извлекаем из него ключ API в переменную api_key.
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']

# Задаем URL API
url = 'https://api.weather.yandex.ru/v2/forecast'

# Создаем базовое окно приложения
app = Tk()

# Добавляем наименование заголовка
app.title("Приложение - запрос погоды")

# Заменяем дефолтную иконку
app.iconbitmap("Images/unik_32x32.ico")

# Устанавливаем изображение из файла в главном окне.
background_image = PhotoImage(file="Images/unik.gif")
# Создаем виджет и публикуем его с указанным изображением
background_label = Label(app, image=background_image)
background_label.pack(fill="both")

# Устанавливаем размер главного окна.
app.geometry("550x800+80+200")

# Команда проверки ввода. register(validate_float) - для окна app регистрирует функцию validate_float,
# которая проверяет поле ввода на тип данных float. %P представляет новое значение, которое передается в функцию проверки.
vinput = (app.register(validate_float), "%P")

# Создаем кнопку для получения координат Кузбасса
b1 = Button(text='Посмотреть координаты городов Кузбасса', font=('Times New Roman', 15), width=36,
            activebackground='black', background='light green', command=Kuzbas)
b1.pack(pady=10)

# Добавляем labels, buttons and text, публикуем виджеты.
city_lat = StringVar()
city_entry_lat = Entry(app, textvariable=city_lat, font=('Times New Roman', 12), validate='key',
                       validatecommand=vinput)  # Ввод с проверкой
city_entry_lat.pack()

h = Label(app, text='(Введите широту)', font=('Times New Roman', 12), wraplength=500)
h.pack()

city_lon = StringVar()
city_entry_lon = Entry(app, textvariable=city_lon, font=('Times New Roman', 12), validate='key',
                       validatecommand=vinput)  # Ввод с проверкой
city_entry_lon.pack()

hc = Label(app, text='(Введите долготу)', font=('Times New Roman', 12), wraplength=500)
hc.pack()

hint_lbl = Label(app, text="Введите в поля ввода координаты для указания расположения.", font=('Times New Roman', 16),
                 wraplength=400)
hint_lbl.pack()

Search_btn = Button(app, text="Запросить погоду по введенным координатам", font=('Times New Roman', 14), width=40,
                    activebackground='yellow', background='light green', command=search)
Search_btn.pack()

location_lbl = Label(app, text="")
location_lbl.pack()

temperature_label = Label(app, text="")
temperature_label.pack()

temperature_alarm_label = Label(app, text="", foreground="red", font=('Times New Roman', 15), wraplength=400)
temperature_alarm_label.pack()

temperature_feel_label = Label(app, text="")
temperature_feel_label.pack()

wind_speed_label = Label(app, text="")
wind_speed_label.pack()

wind_alarm_label = Label(app, text="", foreground="red", font=('Times New Roman', 15), wraplength=400)
wind_alarm_label.pack()

pressure_label = Label(app, text="")
pressure_label.pack()

humidity_label = Label(app, text="")
humidity_label.pack()

condition_label = Label(app, text="")
condition_label.pack()

season_label = Label(app, text="")
season_label.pack()

# Запускаем окно приложения app
app.mainloop()
