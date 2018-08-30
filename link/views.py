from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
import os

from .models import Link
from .serializers import LinkSerializer

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all().order_by('english')
    serializer_class = LinkSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

def link(request):
    links = Link.objects.all().order_by('english')
    return render(request, 'link.html', {'links': links})
