from rest_framework import serializers

from own_packages.clear_string import clear_string
from .models import Country, ContentCountry
from gallery.models import Image


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        # read_only_fields = ('country_url', )


class ContentCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentCountry
        fields = '__all__'
