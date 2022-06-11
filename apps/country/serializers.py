from rest_framework import serializers

from .models import Country, ContentCountry


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        # read_only_fields = ('country_url', )


class ContentCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentCountry
        fields = '__all__'
