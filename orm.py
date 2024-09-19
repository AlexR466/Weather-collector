from database import Session
from models import City, Weather


# Cities
def insert_cities(cities: list[str]) -> None:
    """Добавление городов в таблицу Cities."""
    list_of_city_objects = []
    for city in cities:
        list_of_city_objects.append(City(city_name=city))
    with Session() as db:
        db.add_all(list_of_city_objects)
        db.commit()


# Weather_data
def insert_weather(data: list[str, dict]) -> None:
    """Добавление данных о погоде в таблицу Weather_data."""
    list_of_weather_objects = []
    with Session() as db:
        for city, json in data:
            city_id = db.query(City).filter(
                City.city_name == city
            ).first().city_id
            list_of_weather_objects.append(
                Weather(
                    city_id=city_id,
                    weather_in_city=json
                )
            )
        db.add_all(list_of_weather_objects)
        db.commit()
