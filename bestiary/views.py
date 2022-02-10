from .models import Beast
from django.views.generic import ListView, DetailView


class BeastsListView(ListView):
    model = Beast
    template_name = "bestiary/beasts.html"
    context_object_name = "beasts"


class BeastDetailView(DetailView):
    model = Beast
    template_name = "bestiary/beast.html"
    context_object_name = "beast"
