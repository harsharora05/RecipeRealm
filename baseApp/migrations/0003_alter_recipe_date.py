# Generated by Django 5.0.2 on 2024-02-20 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0002_alter_recipe_category_alter_recipe_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 2, 20, 12, 48, 36, 900534)),
        ),
    ]
