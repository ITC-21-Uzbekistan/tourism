from django.urls import path

from testSerializer.views import CountryCreateView, RetrieveUpdateDestroyCountry, CountryListView, FullCountryView

urlpatterns = [
    path('create/', CountryCreateView.as_view()),
    path('', CountryListView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyCountry.as_view()),
    path('fulls/', FullCountryView.as_view()),
]
