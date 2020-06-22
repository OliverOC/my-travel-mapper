import os
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ollies_travel_hub.settings')

import django
django.setup()

from scratch_map.models import Country


def populate():
    with open('static/geojson/countries.geojson', 'r') as f:
        json_data = json.load(f)

        for feature in json_data['features']:
            country_name = feature['properties']['ADMIN']
            country_code = feature['properties']['ISO_A3']
            country_type = feature['geometry']['type']
            country_coordinates = feature['geometry']['coordinates']

            # New entry
            country = Country.objects.get_or_create(country_name=country_name,
                                                    country_code=country_code,
                                                    country_type=country_type,
                                                    country_coordinates=country_coordinates)[0]


if __name__ == '__main__':
    print("Populating 'Country' database...")
    populate()
    print("Population complete!")

