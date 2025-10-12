from django.db import models

# Create your models here.
class FoodCard(models.Model):
    image = models.ImageField(upload_to='foodCard_images/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    proteins = models.CharField(max_length=20)
    fats = models.CharField(max_length=20)
    carbohydrates = models.CharField(max_length=20)
