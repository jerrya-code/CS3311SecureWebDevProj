from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    return render(request, 'index.html')

def drinks(request):
    return render(request, 'drinks.html')