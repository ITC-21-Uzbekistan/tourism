from rest_framework import serializers
from .models import Language


class LanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class LanguageSer(serializers.Serializer):
    pass