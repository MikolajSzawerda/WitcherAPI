from django.urls import path, include
from . import views

urlpatterns = [
    path('beasts', views.BeastsAPIView.as_view()),
    path('beasts/<int:pk>', views.BeastAPIView.as_view()),
    path('clasifications', views.ClasificationsAPIView.as_view()),
    path('clasifications/<int:pk>', views.ClasificationAPIView.as_view()),
    path('immunities', views.ImmunitiesAPIView.as_view()),
    path('immunities/<int:pk>', views.ImmunityAPIView.as_view()),
    path('weaknesses', views.WeaknessesAPIView.as_view()),
    path('weaknesses/<int:pk>', views.WeaknessAPIView.as_view()),
    path('feeds', views.FeedsAPIView.as_view()),
    path('feeds/<int:pk>', views.FeedAPIView.as_view()),
    path('alchemicals', views.AlchemicalIngredientsAPIView.as_view()),
    path('alchemicals/<int:pk>', views.AlchemicalIngredientAPIView.as_view()),
]
