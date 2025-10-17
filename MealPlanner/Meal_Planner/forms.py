from django import forms
from .models import FoodCard

class FoodCardForm(forms.ModelForm):
    class Meta:
        model = FoodCard
        fields = ['title', 'description', 'category', 'proteins', 'fats', 'carbohydrates', 'image']
