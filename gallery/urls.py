from django.urls import path
from .views import get_images, get_detail_image, create_image, update_image, delete_image

urlpatterns = [
    path('get/', get_images),
    path('get/<int:pk>/', get_detail_image),
    path('create/', create_image),
    path('update/<int:pk>/', update_image),
    path('delete/<int:pk>/', delete_image),
]
