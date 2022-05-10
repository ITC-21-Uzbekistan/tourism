from django.urls import path
from .views import get_images, get_detail_image, create_image, update_image, delete_image
from .image_type import get_types, get_detail_types, create_type, update_type, delete_type

urlpatterns = [
    path('get/', get_images),
    path('get/<int:pk>/', get_detail_image),
    path('create/', create_image),
    path('update/<int:pk>/', update_image),
    path('delete/<int:pk>/', delete_image),

    path('type/get/', get_types),
    path('type/get/<int:pk>/', get_detail_types),
    path('type/create/', create_type),
    path('type/update/<int:pk>/', update_type),
    path('type/delete/<int:pk>/', delete_type),
]
