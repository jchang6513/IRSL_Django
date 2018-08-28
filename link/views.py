from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import os

def link(request):
    return render(request, 'link.html')
