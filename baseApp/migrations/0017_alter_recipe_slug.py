# Generated by Django 5.0.2 on 2024-03-11 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0016_alter_recipe_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(editable=False, max_length=250),
        ),
    ]
