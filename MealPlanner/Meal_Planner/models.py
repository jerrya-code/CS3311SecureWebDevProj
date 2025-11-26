from django.db import models
from django import forms

# Create your models here.
class FoodCard(models.Model):
    category = [
        ('entries', 'Entries'),
        ('salads', 'Salads'),
        ('appetizers', 'Appetizers'),
        ('desserts', 'Desserts'),
        ('drinks', 'Drinks'),
    ]
    image = models.ImageField(upload_to='foodCard_images/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    proteins = models.IntegerField()
    fats = models.IntegerField()
    carbohydrates = models.IntegerField()
    category = models.CharField(max_length=50, choices=category)

    # dietary flags
    gluten_free = models.BooleanField(default=False)
    dairy_free = models.BooleanField(default=False)
    nut_free = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)