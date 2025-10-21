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
    proteins = models.CharField(max_length=20)
    fats = models.CharField(max_length=20)
    carbohydrates = models.CharField(max_length=20)
    category = models.CharField(max_length=50, choices=category, default='entries')