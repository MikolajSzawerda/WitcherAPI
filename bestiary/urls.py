from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<slug:name>', views.beast, name='beast-by-slug')
]
