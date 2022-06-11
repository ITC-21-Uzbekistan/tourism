from django.contrib import admin
from .models import Lang, Country, Content


class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Lang)
admin.site.register(Country, CountryAdmin)
admin.site.register(Content)
