# Generated by Django 3.2.9 on 2022-02-09 17:49

import autoslug.fields
from django.db import migrations

from bestiary.models import Beast


def migrate_data_forward(apps, schema_editor):
    for instance in Beast.objects.all():
        instance.save()

def migrate_data_backward(apps, schema_editor):
    pass



class Migration(migrations.Migration):

    dependencies = [
        ('bestiary', '0004_beast_slug'),
    ]


    operations = [
        migrations.AlterField(
            model_name='beast',
            name='slug',
            field=autoslug.fields.AutoSlugField(null=True, default=None, editable=False, populate_from='name', unique=True),
            preserve_default=False,
        ),
        migrations.RunPython(
            migrate_data_forward,
            migrate_data_backward,
        ),
    ]
