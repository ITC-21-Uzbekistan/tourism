import json

from rest_framework import serializers
from rest_framework.fields import empty
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict

from .models import Lang, Content, Country


class LangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lang
        fields = "__all__"


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'lang', 'country_name', 'country_info']
    #
    # def update(self, instance, validated_data):
    #     instance.country_name = validated_data.get('country_name', instance.country_name)
    #     instance.country_info = validated_data.get('country_info', instance.country_info)
    #     return instance


class CountryCreateSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=True)

    class Meta:
        model = Country
        fields = ['id', 'content', 'name']

    def create(self, validated_data):
        contents_data = validated_data.pop("content")
        country = Country.objects.create(**validated_data)
        for content_data in contents_data:
            Content.objects.create(country=country, **content_data)
        return country

    def update(self, instance, validated_data):
        contents = validated_data.pop("content")
        instance.name = validated_data.get('name', instance.name)

        for content in contents:
            instance_content = Content.objects.get(country=instance, lang_id=content['lang'])
            instance_content.country_name = content.get('country_name', instance_content.country_name)
            instance_content.country_info = content.get('country_info', instance_content.country_info)
            instance_content.save()

        return instance

    # def data(self):
    #     self.instance
    #     return ReturnDict(self.instance, serializer=FullCountrySerializer)


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


class FullCountrySerializer(serializers.ModelSerializer):

    contents = serializers.SerializerMethodField("_get_contents")

    class Meta:
        model = Country
        fields = ('id', 'name', 'contents')

    def _get_contents(self, this):
        contents = Content.objects.filter(country=this)
        serializer = ContentSerializer(contents, many=True)
        return serializer.data
