from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import os

from .models import Research

def research(request):
	context = {
		  'researches' : Research.objects.all()
	}
	return render(request, 'research.html', context)
