from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('delete_card/<str:category>/<int:primary_key>/', views.delete_card, name='delete_card'),
    path('edit_card/<str:category>/<int:primary_key>/', views.edit_card, name='edit_card'),

    path('<str:category>/', views.category_view, name='category'),
]

