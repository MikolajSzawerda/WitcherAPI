# Generated by Django 3.2.9 on 2022-02-10 15:13

from django.db import migrations, models
from bestiary.models import Beast

def assing_slug(*args):
    for obj in Beast.objects.all():
        obj.save()

def assing_img(*arg):
    for obj in Beast.objects.all():
        obj.image.name = f'beasts/{obj.slug}.png'
        obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('bestiary', '0006_auto_20220209_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='beast',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='beasts/'),
        ),
        migrations.RunPython(
            assing_slug,
            assing_img
        )
    ]
# Generated by Django 3.2.9 on 2022-02-10 15:10





