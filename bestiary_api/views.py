from django.shortcuts import render
from rest_framework.generics import ListAPIView
from bestiary.models import Beast
from .serializers import BeastSerializer


class BeastsAPIView(ListAPIView):
    queryset = Beast.objects.all()
    serializer_class = BeastSerializer
