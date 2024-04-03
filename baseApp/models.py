from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from datetime import date


# Create your models here.


class recipe(models.Model):

    CATEGORY_CHOICES =(
        ("BREAKFAST" , "Breakfast"),
        ("LUNCH" ,"Lunch"),
        ("DINNER","Dinner"),
        ("SALAD","Salad"),
        ("STARTER","Starter"),
        ("DESSERT","Dessert"),
        ("DRINK","Drink"),
        ("SOUP","Soup"),
        ("OTHER","Other")
    )
    MEAL_CHOICES =(
        ("VEGETARIAN" , "Vegetarian"),
        ("EGGETARIAN" , "Eggetarian"),
        ("NON-VEGETARIAN" , "Non-Vegetarian"),
    )


    recipeOwner = models.ForeignKey(User,on_delete = models.CASCADE)
    category = models.CharField(choices=CATEGORY_CHOICES,default=None ,max_length=20)
    meal_prefrence = models.CharField(choices=MEAL_CHOICES,default='VEGETARIAN', max_length=20)
    title = models.CharField(max_length = 30)
    ingredients = models.TextField()
    steps = models.TextField()
    recipe_photo=models.ImageField(upload_to='recipePic/')
    famous=models.BooleanField(default=False)
    date= models.DateField(default=date.today())

    def __str__(self):
        return self.title
    


