from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from bestiary.models import (Beast, Clasification, Feed,
                             Weakness, Immunity, AlchemicalIngredient)
from .serializers import (BeastSerializer, ClasificationSerializer,
                          FeedSerializer, WeaknessSerializer,
                          ImmunitySerializer, AlchemicalIngredientSerializer)


class BeastsAPIView(ListAPIView):
    queryset = Beast.objects.all()
    serializer_class = BeastSerializer


class BeastAPIView(APIView):
    def get(self, request, pk):
        obj = Beast.objects.get(pk=pk)
        return Response(BeastSerializer(obj).data)


class ClasificationsAPIView(ListAPIView):
    queryset = Clasification.objects.all()
    serializer_class = ClasificationSerializer


class ClasificationAPIView(APIView):
    def get(self, request, pk):
        obj = Clasification.objects.get(pk=pk)
        return Response(ClasificationSerializer(obj).data)


class FeedsAPIView(ListAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer


class FeedAPIView(APIView):
    def get(self, request, pk):
        obj = Feed.objects.get(pk=pk)
        return Response(FeedSerializer(obj).data)


class WeaknessesAPIView(ListAPIView):
    queryset = Weakness.objects.all()
    serializer_class = WeaknessSerializer


class WeaknessAPIView(APIView):
    def get(self, request, pk):
        obj = Weakness.objects.get(pk=pk)
        return Response(WeaknessSerializer(obj).data)


class ImmunitiesAPIView(ListAPIView):
    queryset = Immunity.objects.all()
    serializer_class = ImmunitySerializer


class ImmunityAPIView(APIView):
    def get(self, request, pk):
        obj = Immunity.objects.get(pk=pk)
        return Response(ImmunitySerializer(obj).data)


class AlchemicalIngredientsAPIView(ListAPIView):
    queryset = AlchemicalIngredient.objects.all()
    serializer_class = AlchemicalIngredientSerializer


class AlchemicalIngredientAPIView(APIView):
    def get(self, request, pk):
        obj = AlchemicalIngredient.objects.get(pk=pk)
        return Response(AlchemicalIngredientSerializer(obj).data)
