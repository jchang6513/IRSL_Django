from rest_framework import serializers
from .models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
#        fields = ('id', 'link', 'photo', 'headline', 'body')
        fields = '__all__'
