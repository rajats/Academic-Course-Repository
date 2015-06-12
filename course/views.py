from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext, Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages

from student.models import Student
from .models import Course, CourseAssignment, CourseSyllabus, CourseLectureNotes, CourseNotice

from userauth.models import RegProfessor, RegStudent

def view_course(request, id):
	if request.user.is_authenticated() and RegStudent.objects.get(user=request.user).active:
		instance = RegStudent.objects.get(user=request.user)
		student = Student.objects.get(name=instance)
		course = Course.objects.get(id=id)
		if course in student.courses.all():
			return render_to_response("course/viewcourse.html", locals(), context_instance=RequestContext(request))
		else:
			raise Http404
	else:
		raise Http404


def add_assignment(request, id):
	pass

def add_syllabus(request, id):
	pass

def add_lecture_notes(request, id):
	pass

def add_notice(request, id):
	pass
