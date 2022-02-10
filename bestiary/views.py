from .models import Beast
from django.views.generic import ListView, DetailView
from .filters import BeastFilter
from typing import Dict, Any


class BeastsListView(ListView):
    model = Beast
    template_name = "bestiary/beasts.html"
    context_object_name = "beasts"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['filter'] = BeastFilter(self.request.GET, queryset=self.get_queryset())
        return context


class BeastDetailView(DetailView):
    model = Beast
    template_name = "bestiary/beast.html"
    context_object_name = "beast"
