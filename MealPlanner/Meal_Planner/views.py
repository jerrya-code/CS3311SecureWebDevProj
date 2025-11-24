from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import FoodCard
from .forms import FoodCardForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import logging
logger = logging.getLogger(__name__)

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
    logger.warning("login_view called: method=%s, path=%s", request.method, request.path)
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            logger.warning("authenticate succeeded for %r", username)
            return redirect('main')
        else:
            logger.warning("authenticate FAILED for %r", username)
            messages.error(request, "Invalid credentials")
            return render(request, 'index.html', {'show_register': False})
    return render(request, 'index.html', {'show_register': False}) 

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username_r', '').strip()
        password = request.POST.get('password_r', '')
        email = request.POST.get('email', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        confirmed_password = request.POST.get('confirm_password', '')

        if confirmed_password != password: 
            messages.error(request, "Passwords do not match")
            return render(request, 'index.html', {'show_register': True})
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken") 
            return render(request, 'index.html', {'show_register': True})

        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password),
            first_name=first_name,
            last_name=last_name
        )
        login(request, user)
        messages.success(request, "Registration successful!")
        return redirect('main')

    return render(request, 'index.html', {'show_register': True})

def logout_view(request):
    logout(request)  
    messages.success(request, "You have been logged out.")
    return redirect('main')  

def add_card(request, category):
    form = FoodCardForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('category', category=category)
    messages.error(request, "Populate all fields")
    return render(request, 'add_card.html', {'form': form, 'category': category})