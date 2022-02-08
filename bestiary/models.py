from django.db import models

# Create your models here.

class Clasification(models.Model):
    name = models.CharField(max_length=250)


class Weakness(models.Model):
    name = models.CharField(max_length=250)


class Distribution(models.Model):
    place = models.CharField(max_length=250)


class Tactics(models.Model):
    description = models.CharField(max_length=500)


class AlchemicalIngredient(models.Model):
    name = models.CharField(max_length=100)


class Feed(models.Model):
    name = models.CharField(max_length=250)


class Immunity(models.Model):
    name = models.CharField(max_length=250)


class Beast(models.Model):
    name = models.CharField(max_length=250)
    nickname = models.CharField(max_length=250, blank=True)
    clasification = models.ForeignKey(Clasification, on_delete=models.CASCADE)
    weaknesses = models.ManyToManyField(Weakness)
    distribution = models.ManyToManyField(Distribution)
    tacticts = models.ForeignKey(Tactics, on_delete=models.CASCADE, blank=True, null=True)
    alchemical_ingredients = models.ManyToManyField(AlchemicalIngredient)
    feed = models.ManyToManyField(Feed)
    immunities = models.ManyToManyField(Immunity)
