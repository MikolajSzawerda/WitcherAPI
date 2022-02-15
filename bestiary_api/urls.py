from django.urls import path, include
from . import views

urlpatterns = [
    path('beasts', views.BeastsAPIView.as_view())
]
