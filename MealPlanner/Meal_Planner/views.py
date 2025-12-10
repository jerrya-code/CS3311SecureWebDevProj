from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import FoodCard
from .forms import FoodCardForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import logging
import random

logger = logging.getLogger(__name__)

def main(request):
    status = request.GET.get("status")  
    username = request.GET.get("user")
    # cart_context = view_cart(request)
    return render(request, 'index.html', {"status":status, "username":username})

def category_view(request, category):
    items = FoodCard.objects.filter(category=category)
    return render(request, 'category.html', {'items': items, 'category': category})

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
            messages.success(request, "User was authenticated successfully")
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

        if username!='' and password!='' and email!='' and first_name!='' and last_name!='' \
            and confirmed_password!='':
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
        else:
            messages.error(request, "Fill out all registration fields!")

    return render(request, 'index.html', {'show_register': True})

def logout_view(request):
    logout(request)  
    messages.success(request, "You have been logged out.")
    return redirect('main')  

def add_card(request, category):
    if request.method == "POST":
        form = FoodCardForm(request.POST, request.FILES)
        if form.is_valid():
            food = form.save(commit=False)   
            food.category = category
            food.save()
            return redirect('category', category=category)
        else:
            messages.error(request, "Populate all fields")
    else:
        form = FoodCardForm()
    return render(request, 'add_card.html', {'form': form, 'category': category})

def add_cart(request, primary_key):
    card = get_object_or_404(FoodCard, pk=primary_key)
    if "cart" not in request.session:
        request.session["cart"] = {}
    cart = request.session["cart"]
    key = str(card.pk)
    if key not in cart:
        cart[key] = 0
    cart[key] += 1
    request.session.modified = True
    return redirect(request.META.get('HTTP_REFERER') or '/')

def clear_cart(request):
    request.session["cart"] = {}
    return redirect(request.META.get('HTTP_REFERER') or '/')

def random_meal(request):
    allEntries = list(FoodCard.objects.filter(category__exact="entries").values('image'))
    allSalads = list(FoodCard.objects.filter(category__exact="salads").values('image'))
    allAppetizers = list(FoodCard.objects.filter(category__exact="appetizers").values('image'))
    allDesserts = list(FoodCard.objects.filter(category__exact="desserts").values('image'))
    allDrinks = list(FoodCard.objects.filter(category__exact="drinks").values('image'))

    categories = [allEntries, allSalads, allAppetizers, allDesserts, allDrinks]
    randomMeal = []

    for category in categories:
        if category:
            randomMeal.append(random.choice(category)['image'])

    data = {'result': randomMeal}
    return JsonResponse(data)
    
