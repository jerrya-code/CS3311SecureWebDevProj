from django import forms
from .models import FoodCard

class FoodCardForm(forms.ModelForm):
    class Meta:
        model = FoodCard
        fields = ['title', 'description', 'proteins', 'fats', 'carbohydrates', 'image']
