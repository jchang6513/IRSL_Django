from rest_framework import serializers
from .models import International, Domestic, Book

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
