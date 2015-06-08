from django.shortcuts import render_to_response, RequestContext, Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages

from course.models import Course 
from userauth.models import RegStudent
from .models import Student

def show_courses(request):
	if request.user.is_authenticated() and RegStudent.objects.get(user=request.user).active:
		try:
			name = RegStudent.objects.get(user=request.user)
			student_sem = RegStudent.objects.get(user=request.user).semester
			student = Student.objects.get(name=name)
		except RegStudent.DoesNotExist:
			student_sem = None
		try:
			courses = Course.objects.filter(semester=student_sem)
			unenrolled_courses = []
			for course in courses:
				if course not in student.courses.all():
					unenrolled_courses.append(course)
		except Course.DoesNotExist:
			courses = None
		return render_to_response("student/enroll.html", locals(), context_instance=RequestContext(request))
	else:
		raise Http404

def enroll(request, id):
	if request.user.is_authenticated() and RegStudent.objects.get(user=request.user).active:
		course = Course.objects.get(id=id)
		student_name = RegStudent.objects.get(user=request.user)
		student = Student.objects.get(name=student_name)
		student.courses.add(course)
		messages.success(request, 'You are enrolled in %s' %(course))
		return HttpResponseRedirect('/student/courses/')
	else:
		raise Http404


