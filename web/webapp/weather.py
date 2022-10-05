from flask import current_app
import requests


def weather_by_city(city_name):
    url = current_app.config['WEATHER_URL']
    params = {
        'key': current_app.config['WEATHER_API_KEY'],
        'q': city_name,
        'format': 'json', 
        'num_of_days': 1,
        'lang': 'ru'
    }
    try:
        result = requests.get(url, params=params)
        result.raise_for_status()
    except(requests.RequestException):
        print("Сетевая ошибка")
        return False

    try:
        weather = result.json()
    except:
        print("Ошибка разбора ответа")
        return False

    if 'data' in weather:
        if 'current_condition' in weather['data']:
            try:
                return weather['data']['current_condition'][0]
            except (IndexError, TypeError):
                return False
    return False


if __name__ == "__main__":
    weather = weather_by_city("Moskow, Russia")
    print(weather)
