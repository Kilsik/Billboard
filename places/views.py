from django.shortcuts import render
from .models import Places, Images


def show_billboards(request):
    places = Places.objects.all()
    features = []
    for place in places:
        feature = {}
        imgs = place.images_set.all()
        images = []
        for img in imgs:
            image = img.img.url
            images.append(image)
        # print(images)
        feature['type'] = "Feature"
        feature['geometry'] = {
            'type': 'Point',
            'coordinates': [place.lng, place.lat]
            }
        feature['properties'] = {
            'title': place.short_title,
            'placeId': place.placeid,
            'detailsUrl': {
                'title': place.title,
                'imgs': images,
                'description_short': place.description_short,
                'description_long': place.description_long,
                'coordinates': {
                    'lng': place.lng,
                    'lat': place.lat
                    }
                }
            }
        features.append(feature)
        geojson = {
            'type': 'FeatureCollection',
            'features': features
            }
        # print(geojson)
    return render(request, 'index.html', context={'geojson': geojson})
