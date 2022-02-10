from django.conf import settings
from django.db import models
from autoslug import AutoSlugField
from django.core.files.storage import FileSystemStorage
# Create your models here.



class Clasification(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Weakness(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Distribution(models.Model):
    place = models.CharField(max_length=250)


class Tactics(models.Model):
    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.description


class AlchemicalIngredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Feed(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Immunity(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Beast(models.Model):
    name = models.CharField(max_length=250)
    nickname = models.CharField(max_length=250, blank=True)
    clasification = models.ForeignKey(Clasification, on_delete=models.CASCADE)
    weaknesses = models.ManyToManyField(Weakness)
    distribution = models.ManyToManyField(Distribution)
    tactics = models.ForeignKey(Tactics, on_delete=models.CASCADE, blank=True, null=True)
    alchemical_ingredients = models.ManyToManyField(AlchemicalIngredient)
    feed = models.ManyToManyField(Feed)
    immunities = models.ManyToManyField(Immunity)
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='name')
    image = models.ImageField(upload_to='beasts/', null=True, blank=True)
