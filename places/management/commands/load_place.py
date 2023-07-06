import requests

from django.core.management.base import BaseCommand
from django.core.exceptions import MultipleObjectsReturned
from django.core.files.base import ContentFile

from places.models import Place, Image


def add_place(loaded_place):
    if ('title' not in loaded_place) or ('coordinates' not in loaded_place)\
            or ('lat' not in loaded_place['coordinates'])\
            or ('lng' not in loaded_place['coordinates']):
        raise KeyError
    place, created = Place.objects.update_or_create(
        title=loaded_place['title'],
        defaults={
            'description_short': loaded_place['description_short'] if 'description_short' in loaded_place else '',
            'description_long': loaded_place['description_long'] if 'description_long' in loaded_place else '',
            'lng': float(loaded_place['coordinates']['lng']),
            'lat': float(loaded_place['coordinates']['lat']),
        }
    )
    return place, created


def load_images(place, img_urls):
    for pos, img_url in enumerate(img_urls):
        file_name = img_url.split('/')[-1]
        response = requests.get(img_url)
        response.raise_for_status()
        img = Image.objects.create(
            position=pos,
            place=place,
        )
        img.img.save(file_name, ContentFile(response.content))
        print(f'Загружено фото {file_name}')
    return None


class Command(BaseCommand):
    help = 'Load data from json-file'

    def add_arguments(self, parser):
        parser.add_argument('json_urls', nargs='+')

    def handle(self, *args, **options):
        for url in options['json_urls']:
            try:
                response = requests.get(url)
                response.raise_for_status()
                loaded_place = response.json()
                place, created = add_place(loaded_place)
                if not created:
                    print(f'Локация {place} обновлена')
                else:
                    print(f'Создана локация {place}')
            except requests.HTTPError as err:
                print(err)
                continue
            except MultipleObjectsReturned:
                print('Существует несколько объектов, соответствующих', url)
                continue
            except KeyError:
                print('Локация не может быть создана без названия и/или координат')
                continue
            img_urls = loaded_place['imgs']
            try:
                load_images(place, img_urls)
            except requests.HTTPError as err:
                print(err)
        return None
