from django.urls import path
from .views import (get_countries, get_detail_country, create_country, update_country,
                    delete_country, RetrieveCountryView, CreateCountryView, ListCountryView,
                    ListContentCountryView, CreateContentCountryView)

urlpatterns = [
    # path('get/', get_countries),
    # path('get/<int:pk>/', get_detail_country),
    # # path('create/', create_country),
    # path('update/<int:pk>/', update_country),
    # path('delete/<int:pk>/', delete_country),
    path('country/<int:pk>/', RetrieveCountryView.as_view(), name="retrieve_country"),
    path('country/', ListCountryView.as_view(), name="list_country"),
    path('country/create/', CreateCountryView.as_view(), name="create_country"),
    path('country/contentcountry/', ListContentCountryView.as_view(), name='content_country_list'),
    path('country/contentcountry/create/', CreateContentCountryView.as_view(), name='content_country_create'),
]
