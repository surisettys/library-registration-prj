# Generated by Django 4.0.4 on 2022-04-18 10:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='bp',
            field=models.IntegerField(default=60, validators=[django.core.validators.MaxValueValidator(300), django.core.validators.MinValueValidator(0)]),
        ),
    ]
