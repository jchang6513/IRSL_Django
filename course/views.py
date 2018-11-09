from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions

from .models import ClassName, Course
from .serializers import ClassNameSerializer, CourseSerializer

class ClassNameViewSet(viewsets.ModelViewSet):
    queryset = ClassName.objects.all().order_by('-id')
    serializer_class = ClassNameSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('class_name')
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

def course(request):
	context = {
		  'ClassNames' : ClassName.objects.all(),
#		  'Course' : Course.objects.all(),
	}

	return render(request, 'course.html', context)
