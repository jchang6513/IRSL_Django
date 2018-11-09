from rest_framework import serializers
from .models import Publication_List, International, Domestic, Book

class PListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication_List
        order_by = (('-id',))
        fields = '__all__'

class InternationaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = International
        order_by = (('-no',))
        fields = ('no', 'year', 'author', 'title', 'paper')

class DomesticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domestic
        order_by = (('-no',))
        fields = ('no', 'year', 'author', 'title', 'paper')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        order_by = (('-no',))
        fields = ('no', 'year', 'author', 'title', 'paper')
