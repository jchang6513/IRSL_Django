from django.shortcuts import render
from django.http import HttpResponse
from .models import Link
from .serializers import LinkSerializer
from rest_framework import viewsets
import os

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all().order_by('english')
    serializer_class = LinkSerializer

def link(request):
    links = Link.objects.all().order_by('english')
    return render(request, 'link.html', {'links': links})
