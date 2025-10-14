from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('menu/<str:category>/', views.category_view, name='category'),
    # Optional shortcut for drinks category
    path('drinks/', views.category_view, {'category': 'drinks'}, name='drinks'),
    
    path('desserts/', views.category_view, {'category': 'desserts'}, name='desserts'),
]
