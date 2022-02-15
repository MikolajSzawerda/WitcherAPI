from dataclasses import field
from .models import Beast, Clasification, Weakness
import django_filters
from django_filters import FilterSet
from django import forms


class BeastFilter(FilterSet):
    clasification = django_filters.ModelMultipleChoiceFilter(
                                                             queryset=Clasification.objects.all(),
                                                             widget=forms.CheckboxSelectMultiple(),
                                                             label="Gatunek")
    weaknesses = django_filters.ModelMultipleChoiceFilter(
                                                             queryset=Weakness.objects.all(),
                                                             widget=forms.CheckboxSelectMultiple(),
                                                             label="Słabości")
    class Meta:
        model = Beast
        fields = ['clasification', 'weaknesses']