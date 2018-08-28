from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import os

from .models import Publication_List, International, Domestic, Book

def pub(request):
    context = {
        'plist'  : Publication_List.objects.all()[0],
        'inters' : International.objects.all().order_by('-NO'),
        'domess' : Domestic.objects.all().order_by('-NO'),
        'books'  : Book.objects.all().order_by('-NO'),
    }
    return render(request, 'pub.html', context)
