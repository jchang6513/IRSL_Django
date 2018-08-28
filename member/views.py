from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import os

from .models import JYLiu_CV
from .models import Member
from .models import Past
from .models import Graduate

def member(request):
	cv   = JYLiu_CV.objects.all()[0]
#	mpds = Member.objects.filter(identity='PD')
#	mfas = Member.objects.filter(identity='FA')
#	mpss = Member.objects.filter(identity='PS')
#	mmss = Member.objects.filter(identity='MS')
	members = Member.objects.all().order_by('english')
	pvps = Past.objects.filter(identity='VP')
	ppds = Past.objects.filter(identity='PD')
	gpds = Graduate.objects.filter(identity='PD')
	gmds = Graduate.objects.filter(identity='MD')
	context = {
		'cv'   : cv,
		'members' : members,
#		'mpds' : mpds,
#		'mfas' : mfas,
#		'mpss' : mpss,
#		'mmss' : mmss,
		'pvps' : pvps,
		'ppds' : ppds,
		'gpds' : gpds,
		'gmds' : gmds,
	}
	return render(request, 'member.html', context)


