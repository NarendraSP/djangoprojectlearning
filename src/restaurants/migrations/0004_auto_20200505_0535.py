# Generated by Django 3.0.5 on 2020-05-05 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20200505_0532'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RestaurantLocations',
            new_name='RestaurantLocation',
        ),
    ]
