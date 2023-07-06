from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from .models import Place


def show_billboards(request):
    places = Place.objects.all()
    features = []
    for place in places:
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.title,
                'placeId': place.pk,
                'detailsUrl': reverse('show-detail', kwargs={'place_id': place.pk})
            }
        }
        features.append(feature)

    context = {
        'geojson': {
            'type': 'FeatureCollection',
            'features': features
        }
    }
    return render(request, 'index.html', context=context)


def show_place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    imgs = place.images.all()
    images = [img.img.url for img in imgs]
    details = {
        'title': place.title,
        'imgs': images,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    return JsonResponse(details, json_dumps_params={'ensure_ascii': False})
