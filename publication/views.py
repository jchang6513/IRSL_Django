from django.shortcuts import render
from rest_framework import viewsets, permissions
# Create your views here.

from django.http import HttpResponse
import os

from .serializers import InternationaleSerializer, DomesticSerializer, BookSerializer
from .models import Publication_List, International, Domestic, Book

class InternationalViewSet(viewsets.ModelViewSet):
    queryset = International.objects.all().order_by('-no')
    serializer_class = InternationaleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DomesticViewSet(viewsets.ModelViewSet):
    queryset = Domestic.objects.all().order_by('-no')
    serializer_class = DomesticSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-no')
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

def pub(request):
    context = {
        'plist'  : Publication_List.objects.last(),
        'inters' : International.objects.all().order_by('-no'),
        'domess' : Domestic.objects.all().order_by('-no'),
        'books'  : Book.objects.all().order_by('-no'),
    }
    return render(request, 'pub.html', context)
