# Generated by Django 3.0.5 on 2020-05-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_restaurantlocation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]