from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import os

def intro(request):
    return render(request, 'intro.html')
