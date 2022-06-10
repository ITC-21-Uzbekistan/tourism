from django.contrib import admin
from .models import ContentCountry, Country


class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'country_name', 'country_url', 'country_meta_keywords']


class ContentCountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'country', 'language', 'country_name', 'country_info']


admin.site.register(Country, CountryAdmin)
admin.site.register(ContentCountry, ContentCountryAdmin)
