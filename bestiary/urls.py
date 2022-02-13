from django.urls import path
from . import views


urlpatterns = [
    path('', views.BeastsListView.as_view(), name='beasts-list'),
    path('favourite', views.FavouriteBeast.as_view()),
    path('<slug:slug>', views.BeastDetailView.as_view(), name='beast-by-slug'),
]
