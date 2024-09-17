import requests

from coordinates import cities_coordinates
from config import API_KEY, PARAMETRES, URL


def find_weather(city, lat, lng):
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
    except Exception:
        print('Ошибка ответа от Api')
    weather = response.json()['data']['weatherByPoint']['now']
    print(city)
    for parametr in PARAMETRES.split():
        print(parametr, weather[parametr])


for city, [lat, lng] in cities_coordinates.items():
    find_weather(city, lat, lng)
