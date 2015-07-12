from django.shortcuts import render_to_response, RequestContext, Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages

from course.models import Course 
from userauth.models import RegProfessor

def my_teaching_courses(request):
	"""
	Shows the courses to professor for which he/she is instructor
	"""
	if request.user.is_authenticated() and RegProfessor.objects.get(user=request.user).active:
		reg_professor = RegProfessor.objects.get(user=request.user)
		courses = Course.objects.filter(instructor=reg_professor)
		return render_to_response("professor/myteachingcourses.html", locals(), context_instance=RequestContext(request))
	else:
		raise Http404

