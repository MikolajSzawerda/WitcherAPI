from .models import Beast
from django_filters import FilterSet

class BeastFilter(FilterSet):
    class Meta:
        model = Beast
        fields = ['clasification', 'weaknesses']