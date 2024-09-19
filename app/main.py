from threading import Timer

from config import LIST_OF_CITIES, RETRY_PERIOD
from helpers.weather import find_weather_in_cities
from orm import insert_cities, insert_weather


def repeater(interval: int, function) -> None:
    """
    Реализация цикличного выполнения функции
    через указанный интервал времени.
    """
    Timer(interval, repeater, [interval, function]).start()
    function()


def weather() -> None:
    insert_weather(find_weather_in_cities())


def main():
    insert_cities(LIST_OF_CITIES)
    repeater(RETRY_PERIOD, weather)


if __name__ == '__main__':
    main()
