from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import os

from news.models import News

def home(request):
    newss = News.objects.all().order_by('-date')[0:3]
    context = {
        'newss' : newss
    }
    return render(request, 'index.html', context)
