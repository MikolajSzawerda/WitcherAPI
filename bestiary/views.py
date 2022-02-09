from django.shortcuts import render
from django.http import HttpResponse
from .models import Beast


def index(req):
    beasts = Beast.objects.all()
    beasts_data = [(b.name, b.slug) for b in beasts]
    return render(req, 'bestiary/beasts.html',{
        "beasts": beasts_data
    })


def beast(req, name):
    beast = Beast.objects.get(slug=name)
    return render(req, 'bestiary/beast.html', {
        'beast': beast
    })
