from rest_framework import serializers
from .models import Country, ContentCountry


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class ContentCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentCountry
        fields = '__all__'
