from django.shortcuts import render
from django.http import HttpResponse
from .serializers import JYLSerializer, MemberSerializer, PastSerializer, GraduateSerializer
from .models import JYLiu_CV, Member, Past, Graduate
from rest_framework import viewsets, permissions
import os

class JYLViewSet(viewsets.ModelViewSet):
    queryset = JYLiu_CV.objects.all()
    serializer_class = JYLSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().order_by('-chinese')
    serializer_class = MemberSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PastViewSet(viewsets.ModelViewSet):
    queryset = Past.objects.all()
    serializer_class = PastSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class GraduateViewSet(viewsets.ModelViewSet):
    queryset = Graduate.objects.all()
    serializer_class = GraduateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

def member(request):
	cv   = JYLiu_CV.objects.all()[0]
	members = Member.objects.all().order_by('english')
	pvps = Past.objects.filter(identity='VP')
	ppds = Past.objects.filter(identity='PD')
	gpds = Graduate.objects.filter(identity='PD')
	gmds = Graduate.objects.filter(identity='MD')
	context = {
		'cv'   : cv,
		'members' : members,
		'pvps' : pvps,
		'ppds' : ppds,
		'gpds' : gpds,
		'gmds' : gmds,
	}
	return render(request, 'member.html', context)
