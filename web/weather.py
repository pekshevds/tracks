import requests


def weather_by_city(city_name):
    url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        'key': '3ee7edd3364d4635a6055621220410',
        'q': city_name,
        'format': 'json', 
        'num_of_days': 1,
        'lang': 'ru'
    }
    result = requests.get(url, params=params)
    weather = result.json()

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
