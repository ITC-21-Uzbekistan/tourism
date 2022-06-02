from rest_framework import serializers
from .models import Region, ContentRegion


class RegionSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField('_get_content')

    def _get_content(self, lang, region_region):
        try:
            ContentRegion.objects.get(language__language_short=lang, region__id=self.id)
        except Exception as ex:
            print(ex)

    class Meta:
        model = Region
        fields = ['id', 'region_name', 'region_info', 'region_url', 'region_meta_keywords', 'country', 'region_images']
        depth = 2
