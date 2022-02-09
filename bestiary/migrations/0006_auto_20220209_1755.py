# Generated by Django 3.2.9 on 2022-02-09 17:55

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bestiary', '0005_alter_beast_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beast',
            old_name='tacticts',
            new_name='tactics',
        ),
        migrations.AlterField(
            model_name='beast',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
    ]