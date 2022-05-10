from django.urls import path
from .views import get_countries, create_country, update_country, delete_country

urlpatterns = [
    path('get/', get_countries),
    path('get/<int:pk>/', get_countries),
    path('create/', create_country),
    path('update/<int:pk>/', update_country),
    path('delete/<int:pk>/', delete_country),
]
