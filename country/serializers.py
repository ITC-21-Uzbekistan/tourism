from rest_framework import serializers

from own_packages.clear_string import clear_string
from .models import Country, ContentCountry


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        read_only_fields = ('country_url', )

    def create(self, validated_data):
        country_url = validated_data.pop('country_url', None)
        instance = self.Meta.model(**validated_data)
        instance.country_url = clear_string(instance.country_name)
        instance.save()
        return instance


class ContentCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentCountry
        fields = '__all__'
