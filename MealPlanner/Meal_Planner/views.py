#from pyexpat.errors import messages
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import FoodCard
from .forms import FoodCardForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

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
        username = request.POST['username_r']
        password = request.POST['password_r']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        confirmed_password = request.POST['confirm_password']
        if confirmed_password != password: return render(request, 'index.html', {'error': 'Passwords do not match'})
        if User.objects.filter(username=username).exists(): return render(request, 'index.html', {'error': 'Username already taken'})

        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password),
            first_name=first_name,
            last_name=last_name
        )
        request.session['user_id'] = user.id
        return render(request, 'index.html', {'success': 'Account created successfully!'})

    return render(request, 'index.html')
