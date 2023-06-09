from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from .models import Places


def show_billboards(request):
    places = Places.objects.all()
    features = []
    for place in places:
        feature = {}

        feature['type'] = "Feature"
        feature['geometry'] = {
            'type': 'Point',
            'coordinates': [place.lng, place.lat]
            }
        feature['properties'] = {
            'title': place.short_title,
            'placeId': place.placeid,
            'detailsUrl': reverse('show-detail', kwargs={'placeid': place.pk})
            }
        features.append(feature)
        geojson = {
            'type': 'FeatureCollection',
            'features': features
            }
    return render(request, 'index.html', context={'geojson': geojson})


def show_place_detail(request, placeid):
    place = get_object_or_404(Places, pk=placeid)
    imgs = place.images_set.all()
    images = []
    for img in imgs:
        image = img.img.url
        images.append(image)
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
