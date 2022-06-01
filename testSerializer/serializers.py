from rest_framework import serializers
from rest_framework.fields import empty
from rest_framework.response import Response
from .models import Lang, Content, Country


class LangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lang
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    country_name = serializers.SerializerMethodField('_get_name')
    country_info = serializers.SerializerMethodField('_get_info')

    class Meta:
        model = Country
        fields = ['id', 'country_name', 'country_info']

    def _get_name(self, this):
        country_name = Content.objects.get(country__id=this.id, lang__short=str(self.context.get('lang')))
        return country_name.country_name

    def _get_info(self, this):
        country_info = Content.objects.get(country__id=this.id, lang__short=str(self.context.get('lang')))
        return country_info.country_info


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'lang', 'country', 'country_name', 'country_info']
