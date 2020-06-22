import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ollies_travel_hub.settings')

import django
django.setup()

from scratch_map.models import Trip
from faker import Faker

fakegen = Faker()


def populate(N=1):
    for entry in range(N):
        fake_country = fakegen.country()
        fake_year = fakegen.year()
        fake_comment = fakegen.sentence()

        # New entry
        trip = Trip.objects.get_or_create(country_visited=fake_country,
                                           year_visited=fake_year,
                                           comment=fake_comment)[0]


if __name__ == '__main__':
    print("Populating 'Trip' database...")
    populate(20)
    print("population complete!")

