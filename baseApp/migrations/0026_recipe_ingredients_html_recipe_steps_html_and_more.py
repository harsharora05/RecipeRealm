# Generated by Django 5.0.4 on 2024-06-12 08:41

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0025_recipe_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients_HTML',
            field=tinymce.models.HTMLField(default='html'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='steps_HTML',
            field=tinymce.models.HTMLField(default='html'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='steps',
            field=models.CharField(max_length=3000),
        ),
    ]
