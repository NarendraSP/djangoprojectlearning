# Generated by Django 3.0.5 on 2020-05-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20200505_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
