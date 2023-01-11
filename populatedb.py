from suggestion.models import City
import json


def populate_db():
    with open("data.json", "r") as file:
        file_json = file.read()
        cities = json.loads(file_json)
        for city in cities:
            name = f"{city['name']}, {city['countryCode']}"
            longitude = city["lng"]
            latitude = city["lat"]
            City.objects.create(name=name, longitude=longitude, latitude=latitude)
