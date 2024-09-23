# В этом файле хранятся данные о городах, в которых требуется узнать погоду,
# а также требуемые параметры для поиска
from dotenv import load_dotenv
import os

from helpers.cities import get_top_cities

# Период обновления данных о погоде.
RETRY_PERIOD = 20
# LIST_OF_CITIES - список городов.
LIST_OF_CITIES = None
NUMBER_OF_TOP_CITIES = 10
if LIST_OF_CITIES is None:
    LIST_OF_CITIES = get_top_cities(NUMBER_OF_TOP_CITIES)

# Переменная содержит искомые параметры погоды.
# Параметры необходимо указать в строке через пробел
# Возможные параметры:
# температура – temperature,
# влажность воздуха – humidity,
# давление – pressure,
# тип и сила осадков – precType, precStrength,
# скорость и направление ветра – windSpeed, windDirection,
# облачность – cloudiness
PARAMETRES = 'temperature humidity pressure'

# URL для АПИ Яндекс.Погода.
URL = 'https://api.weather.yandex.ru/graphql/query'


load_dotenv()
API_KEY = os.environ.get('API_KEY')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_DB = os.environ.get('POSTGRES_DB')
