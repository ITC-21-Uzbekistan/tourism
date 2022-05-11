from rest_framework import serializers
from .models import TypeImage, Image


class TypeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeImage
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
