from audioop import reverse
from django.http import HttpResponseRedirect
from .models import Beast
from django.views.generic import ListView, DetailView, View
from .filters import BeastFilter
from typing import Dict, Any


class BeastsListView(ListView):
    model = Beast
    template_name = "bestiary/beasts.html"
    context_object_name = "beasts"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['filter'] = BeastFilter(self.request.GET, queryset=self.get_queryset())
        context['fav_ids'] = self.request.session.get('fav', list())
        return context


class BeastDetailView(DetailView):
    model = Beast
    template_name = "bestiary/beast.html"
    context_object_name = "beast"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        fav_ids = self.request.session.get('fav', list())
        context['isfav'] = (self.object.id in fav_ids)
        context['distribution'] = self.object.distribution.first()
        context['data'] = (
            {
                'title': "Słabości",
                'objs': self.object.weaknesses.all()
            },
            {
                'title': "Składniki alchemiczne",
                'objs': self.object.alchemical_ingredients.all()
            },
            {
                'title': "Pożywienie",
                'objs': self.object.feed.all()
            },
            {
                'title': "Odporności",
                'objs': self.object.immunities.all()
            },
        )
        return context


class FavouriteBeast(View):
    model = Beast

    def post(self, request):
        beast_id = int(request.POST['beast_id'])
        ids_list = request.session.get('fav', list())
        try:
            ids_list.remove(beast_id)
        except ValueError:
            ids_list.append(beast_id)
        except AttributeError:
            request.session['fav'] = list()
        request.session['fav'] = ids_list
        return HttpResponseRedirect('/beasts/')
