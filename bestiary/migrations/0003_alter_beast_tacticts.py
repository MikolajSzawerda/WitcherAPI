# Generated by Django 3.2.9 on 2022-02-08 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bestiary', '0002_alter_beast_tacticts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beast',
            name='tacticts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bestiary.tactics'),
        ),
    ]