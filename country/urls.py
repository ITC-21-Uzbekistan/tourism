from django.urls import path
from .views import get_countries, get_detail_country, create_country, update_country, delete_country

urlpatterns = [
    path('get/', get_countries),
    path('get/<int:pk>/', get_detail_country),
    path('create/', create_country),
    path('update/<int:pk>/', update_country),
    path('delete/<int:pk>/', delete_country),
]
