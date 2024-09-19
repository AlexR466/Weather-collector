from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent='Weather-collector')


def find_coordinates(list_of_cities: list) -> dict:
    """Поиск координат списка городов."""
    cities_coordinates = {}
    for city in list_of_cities:
        location = geolocator.geocode(city)
        lat = location.latitude
        lng = location.longitude
        cities_coordinates[city] = [lat, lng]
    return cities_coordinates
