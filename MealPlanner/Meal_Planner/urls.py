from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('/<str:category>/', views.category_view, name='category'),
]
