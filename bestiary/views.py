from django.shortcuts import render
from django.http import HttpResponse
from .models import Beast


def index(req):
    obj = Beast.objects.get(pk=1)

    return HttpResponse(obj.name)
