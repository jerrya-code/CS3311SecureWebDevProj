from django.http import HttpResponse
from django.shortcuts import render
from .models import FoodCard

def main(request):
    return render(request, 'index.html')

def category_view(request, category):
    items = FoodCard.objects.filter(category=category)
    return render(request, f'{category}.html', {'items': items, 'category': category})