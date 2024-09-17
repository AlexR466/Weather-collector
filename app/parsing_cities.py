import requests
from bs4 import BeautifulSoup


def get_top_cities(number_of_cities: int) -> list[str]:
    """
    Функция для парсинга крупнейших городов со страницы в Википедии.
    """
    url = "https://en.wikipedia.org/wiki/List_of_largest_cities"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})

    cities = []
    for row in table.find_all('tr')[2:2+number_of_cities]:
        cols = row.find_all('th', scope='row')
        city = cols[0].find('a')
        cities.append(city.get_text())

    return cities
