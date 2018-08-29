from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Link
import os

def link(request):
    links = Link.objects.all().order_by('id')
    
    return render(request, 'link.html', {'links': links})
