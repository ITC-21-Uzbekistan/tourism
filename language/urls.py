from django.urls import path, include
from .views import ListCreateLanguageView, UpdateDestroyLanguageView

urlpatterns = [
    path('uz/', include("country.urls")),
    path('ru/', include("country.urls")),
    path('lang/', ListCreateLanguageView.as_view(), name="list_create_lang"),
    path('lang/<int:pk>/', UpdateDestroyLanguageView.as_view(), name="update_destroy_lang"),
]
