from attr import fields
from bestiary.models import (Beast, Clasification, Feed,
                             Weakness, Immunity, AlchemicalIngredient)
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class BeastSerializer(ModelSerializer):
    class Meta:
        model = Beast
        depth = 1
        fields = '__all__'


class ClasificationSerializer(ModelSerializer):
    class Meta:
        model = Clasification
        fields = '__all__'


class FeedSerializer(ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'


class WeaknessSerializer(ModelSerializer):
    class Meta:
        model = Weakness
        fields = '__all__'


class ImmunitySerializer(ModelSerializer):
    class Meta:
        model = Immunity
        fields = '__all__'


class AlchemicalIngredientSerializer(ModelSerializer):
    class Meta:
        model = AlchemicalIngredient
        fields = '__all__'

