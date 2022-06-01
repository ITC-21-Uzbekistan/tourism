from django.urls import path

from testSerializer.views import CountryAPIView, RetrieveUpdateDestroyCountry

urlpatterns = [
    path('', CountryAPIView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyCountry.as_view()),
]
