from dataclasses import field

from attr import fields
from bestiary.models import Beast, Tactics
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class BeastSerializer(ModelSerializer):
    class Meta:
        model = Beast
        depth = 1
        fields = '__all__'
