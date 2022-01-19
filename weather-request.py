import requests
from pprint import pprint
import datetime
from config import open_weather_token


def get_weahter(city, open_weather_token):

    code_to_emoji = {
        "Clear": "Ясно \U00002600 ",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь U0001F327",
        "Drizzle": "Морось \U00002614",
        "Thunderstorm": "Гроза 	\U000026C8",
        "Snow": "Снег \U0001F328 \U0000FE0F",
        "Mist": "Туман \U0000FE0F",
        "Smoke": "Дымка \U0001F301",
        "Haze": "Дымка \U0001F301",
        "Dust": "Пыль",
        "Fog": "Туман \U0001F301",
        "Sand": "Песок",
        "Ash": "Пепел",
        "Squall": "Вихрь \U0001F32A",
        "Tornado": "Торнадо \U0001F32A"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        pprint(data)

        city = data["name"]
        temp = data["main"]["temp"]

        weather_discription = data["weather"][0]["main"]
        if weather_discription in code_to_emoji:
            wd = code_to_emoji[weather_discription]
        else:
            wd = "Не удалось выяснить"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        sys_sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sys_sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        print(
            f"Погода в {city} на данный момент "
            f"{wd}\n"
            f"Тепература: {temp}\n"
            f"Влажность: {humidity}\n"
            f"Атмосферное давление: {pressure}\n"
            f"Скорость ветра: {wind_speed}\n"
        )

    except Exception as ex:
        print(ex)
        print("Ошибка: проверьте правильность ввода")


def main():
    city = input("Введите город:")
    get_weahter(city, open_weather_token)


if __name__ == '__main__':
    main()
