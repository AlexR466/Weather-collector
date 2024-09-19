import requests

from config import API_KEY, LIST_OF_CITIES, PARAMETRES, URL
from helpers.coordinates import find_coordinates


def find_weather(lat: float, lng: float) -> dict:
    """Поиск погоды в заданных координатах"""
    headers = {
        "X-Yandex-Weather-Key": API_KEY
    }
    query = f"""{{
    weatherByPoint(request: {{ lat: {lat}, lon: {lng} }}) {{
    now {{
        {PARAMETRES}
    }}
    }}
    }}"""
    try:
        response = requests.post(
            URL,
            headers=headers,
            json={'query': query}
        )
        weather = response.json()['data']['weatherByPoint']['now']
        return weather
    except Exception as exp:
        print(f'Ошибка ответа от Api: {exp}')


def find_weather_in_cities() -> list[str, dict]:
    """
    Поиск погоды в списке городов, указанных
    в переменной LIST_OF_CITIES в файле config.py.
    """
    list_of_data = []
    for city, [lat, lng] in find_coordinates(LIST_OF_CITIES).items():
        list_of_data.append([city, find_weather(lat, lng)])
    return list_of_data
