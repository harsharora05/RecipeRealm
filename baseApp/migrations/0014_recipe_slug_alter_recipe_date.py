# Generated by Django 5.0.2 on 2024-03-11 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0013_alter_recipe_recipe_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 11)),
        ),
    ]