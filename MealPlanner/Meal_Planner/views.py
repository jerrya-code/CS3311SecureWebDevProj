#from pyexpat.errors import messages
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import FoodCard
from .forms import FoodCardForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login

def main(request):
    return render(request, 'index.html')

def category_view(request, category):
    items = FoodCard.objects.filter(category=category)
    return render(request, f'{category}.html', {'items': items, 'category': category})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_card(request, category, primary_key):
    card = get_object_or_404(FoodCard, pk=primary_key)
    card.delete()
    return redirect('category', category=category)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_card(request, category, primary_key):
    card = get_object_or_404(FoodCard, pk=primary_key)
    if request.method == 'POST':
        form = FoodCardForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            form.save()
            return redirect('category', category=category)
    else:
        form = FoodCardForm(instance=card)
    
    return render(request, 'edit_card.html', {'form': form, 'card': card})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'index.html') 

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'index.html', {'form': form})