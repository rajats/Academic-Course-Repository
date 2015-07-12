from django.shortcuts import render_to_response, RequestContext, Http404,HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count

from userauth.models import RegStudent, RegProfessor

def home(request):
	"""
	Shows the home page of Academic Course Repository with option for Login and Registration
	"""
	if RegStudent.objects.filter(user=request.user.id).exists():
		reg_student = RegStudent.objects.get(user=request.user)
	elif RegProfessor.objects.filter(user=request.user.id).exists():
		reg_professor = RegProfessor.objects.get(user=request.user)
	return render_to_response("home.html", locals(), context_instance=RequestContext(request))


