from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('delete_card/<str:category>/<int:primary_key>/', views.delete_card, name='delete_card'),

    path('add_card/<str:category>', views.add_card, name='add_card'),
    path('edit_card/<str:category>/<int:primary_key>/', views.edit_card, name='edit_card'),
    
    path('<int:primary_key>/add/', views.add_cart, name='add_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),

    path('ajax/random-meal/', views.random_meal, name='random_meal'),

    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'Meal_Planner/imgs/chef_hat.png')),

    path('category/<str:category>/', views.category_view, name='category'),
]

