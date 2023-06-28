import requests

from django.core.management.base import BaseCommand
from django.core.exceptions import MultipleObjectsReturned
from slugify import slugify
from django.core.files.base import ContentFile

from places.models import Places, Images


def add_place(url):
    response = requests.get(url)
    response.raise_for_status()
    place_json = response.json()
    place, created = Places.objects.get_or_create(
        title=place_json['title'],
        short_title=place_json['title'],
        description_short=place_json['description_short'],
        description_long=place_json['description_long'],
        lng=float(place_json['coordinates']['lng']),
        lat=float(place_json['coordinates']['lat']),
        )
    return place, created, place_json['imgs']


class Command(BaseCommand):
    help = 'Load data from json-file'

    def add_arguments(self, parser):
        parser.add_argument('json_urls', nargs='+')

    def handle(self, *args, **options):
        for url in options['json_urls']:
            try:
                place, created, img_urls = add_place(url)
                if not created:
                    print(f'Локация {place} уже существует')
                else:
                    print(f'Создана локация {place}')
            except requests.HTTPError as err:
                print(err)
            except MultipleObjectsReturned:
                print('Существует несколько объектов, соответствующих', url)

            for pos, img_url in enumerate(img_urls):
                try:
                    response = requests.get(img_url)
                    response.raise_for_status()
                except requests.HTTPError as err:
                    print(err)
                file_name = img_url.split('/')[-1]
                img = Images.objects.create(
                    position=pos,
                    place=place,
                    )
                img.img.save(file_name, ContentFile(response.content))
                print(f'Загружено фото {file_name}')
        return None
