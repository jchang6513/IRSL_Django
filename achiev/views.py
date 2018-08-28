from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import os

def achiev(request):
    return render(request, 'achiev.html')
