from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import os

from .models import Conference, Oral

def conf(request):
    context = {
		'confs' : Conference.objects.all(),
		'orals' : Oral.objects.all(),
    }
    return render(request, 'conf.html', context)
