# В этом файле хранятся данные о городах, в которых требуется узнать погоду,
# а также требуемые параметры для поиска
from dotenv import load_dotenv
import os
from parsing_cities import get_top_cities

CITIES = None
NUMBER_OF_TOP_CITIES = 10
PARAMETRES = 'temperature humidity'
URL = 'https://api.weather.yandex.ru/graphql/query'


if CITIES is None:
    CITIES = get_top_cities(NUMBER_OF_TOP_CITIES)
load_dotenv()
API_KEY = os.environ.get('API_KEY')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_NAME = os.environ.get('DB_NAME')
