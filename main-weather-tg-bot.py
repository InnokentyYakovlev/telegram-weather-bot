import requests
from config import open_weather_token, tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Укажите название города для вывода погоды")


@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
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
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        temp = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Не удалось установить погоду"

        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]

        await message.answer(f"Погода в {city} на данный момент\n"
                             f"\n"
                             f"{wd}\n"
                             f"Тепература: {temp} °C\n"
                             f"Ощущается как: {feels_like} °C\n"
                             f"Влажность: {humidity}%\n"
                             f"Атмосферное давление: {pressure} мм рт. ст.\n"
                             f"Скорость ветра: {wind_speed} м/с")


    except:
        await message.reply("Проверьте название города")


if __name__ == '__main__':
    executor.start_polling(dp)
