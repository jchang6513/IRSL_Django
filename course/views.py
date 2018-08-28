from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import os

from .models import ClassName, Course

def course(request):
	context = {
		  'ClassNames' : ClassName.objects.all(),
#		  'Course' : Course.objects.all(),
	}
	
	return render(request, 'course.html', context)
