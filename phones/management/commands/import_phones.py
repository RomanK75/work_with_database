import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Add the phone models from csv to my db'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            new_phone = Phone(
                id = phone['id'],
                name = phone['name'],
                price = phone['price'],
                image = phone['image'],
                release_date = phone['release_date'],
                lte_exists = phone['lte_exists'],
                slug = phone['name'].strip().lower().replace(' ','-')
                )
            new_phone.save()
            # print(phone)
            self.stdout.write(f"ID({phone['id']}){phone['name']} -- was added from csv to DB")
