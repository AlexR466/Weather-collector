from geopy.geocoders import Nominatim

from config import CITIES

geolocator = Nominatim(user_agent='Weather-collector')
cities_coordinates = {}
for city in CITIES:
    location = geolocator.geocode(city)
    lat = location.latitude
    lng = location.longitude
    cities_coordinates[city] = [lat, lng]
