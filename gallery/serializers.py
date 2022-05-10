from rest_framework import serializers
from .models import TypeImage


class TypeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeImage
        fields = '__all__'


# class ImageSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     country = serializers.IntegerField()
#     region = serializers.IntegerField()
#     shrine = serializers.IntegerField()
#     tour = serializers.IntegerField()
#     type = serializers.IntegerField()
#
#     name = serializers.CharField(max_length=255, required=True)
#     img = serializers.CharField(required=True)
#     alt_text = serializers.CharField(max_length=500)
#     description = serializers.CharField(required=False)
#
#
# class GetImageSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     country = serializers.IntegerField()
#     region = serializers.IntegerField()
#     shrine = serializers.IntegerField()
#     tour = serializers.IntegerField()
#     type = serializers.IntegerField()
#
#     image = serializers.FileField()
#     alt_text = serializers.CharField()
#     description = serializers.CharField()