from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import os

from .models import News
def news(request):
    newss = News.objects.all().order_by('-date')
    context = {
        'newss' : newss
    }
    return render(request, 'news.html', context)