from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext, Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone

from student.models import Student
from .models import Course, CourseAssignment, CourseSyllabus, CourseLectureNotes, CourseNotice
from .forms import CourseAssignmentForm, CourseSyllabusForm, CourseLectureNotesForm, CourseNoticeForm

from userauth.models import RegProfessor, RegStudent

def view_course(request, id):
	if request.user.is_authenticated():
		course = Course.objects.get(id=id)
		if RegStudent.objects.filter(user=request.user.id).exists():
			if RegStudent.objects.get(user=request.user).active:
				reg_student = RegStudent.objects.get(user=request.user)
				student = Student.objects.get(name=reg_student)
				if course in student.courses.all():
					return render_to_response("course/viewcourse.html", locals(), context_instance=RequestContext(request))
		elif RegProfessor.objects.filter(user=request.user.id).exists():
			if RegProfessor.objects.get(user=request.user).active:
				reg_professor = RegProfessor.objects.get(user=request.user)
				if course in Course.objects.filter(instructor=reg_professor):
					return render_to_response("course/viewcourse.html", locals(), context_instance=RequestContext(request))
		else:
			raise Http404
	else:
		raise Http404

def view_assignment(request, id):
	if request.user.is_authenticated():
		course = Course.objects.get(id=id)
		assignments = CourseAssignment.objects.filter(course=course)
		if RegStudent.objects.filter(user=request.user.id).exists():
			if RegStudent.objects.get(user=request.user).active:
				reg_student = RegStudent.objects.get(user=request.user)
				student = Student.objects.get(name=reg_student)
				if course in student.courses.all():
					return render_to_response("course/viewassignment.html", locals(), context_instance=RequestContext(request))
				else:
					raise Http404
		elif RegProfessor.objects.filter(user=request.user.id).exists():
			if RegProfessor.objects.get(user=request.user).active:
				reg_professor = RegProfessor.objects.get(user=request.user)
				if course in Course.objects.filter(instructor=reg_professor):
					return render_to_response("course/viewassignment.html", locals(), context_instance=RequestContext(request))
				else:
					raise Http404
		else:
			raise Http404
	else:
		raise Http404


def add_assignment(request, id):
	if request.user.is_authenticated() and RegProfessor.objects.get(user=request.user).active:
		reg_professor = RegProfessor.objects.get(user=request.user)
		course = Course.objects.get(id=id)
		if course.instructor == reg_professor:
			form = CourseAssignmentForm(request.POST or None)
			if form.is_valid():
				description = form.cleaned_data['description']
				assignment = form.cleaned_data['assignment']
				deadline = form.cleaned_data['deadline']
				CourseAssignment.objects.create(course=course, description=description, assignment=assignment, deadline=deadline, timestamp=timezone.now())
		return render_to_response("course/addassignment.html", locals(), context_instance=RequestContext(request))
	else:
		raise Http404

def view_syllabus(request, id):
	if request.user.is_authenticated():
		course = Course.objects.get(id=id)
		syllabuses = CourseSyllabus.objects.filter(course=course)
		if RegStudent.objects.filter(user=request.user.id).exists():
			if RegStudent.objects.get(user=request.user).active:
				reg_student = RegStudent.objects.get(user=request.user)
				student = Student.objects.get(name=reg_student)
				if course in student.courses.all():
					return render_to_response("course/viewsyllabus.html", locals(), context_instance=RequestContext(request))
				else:
					raise Http404
		elif RegProfessor.objects.filter(user=request.user.id).exists():
			if RegProfessor.objects.get(user=request.user).active:
				reg_professor = RegProfessor.objects.get(user=request.user)
				if course in Course.objects.filter(instructor=reg_professor):
					return render_to_response("course/viewsyllabus.html", locals(), context_instance=RequestContext(request))
				else:
					raise Http404
		else:
			raise Http404
	else:
		raise Http404

def add_syllabus(request, id):
	pass

def add_lecture_notes(request, id):
	pass

def add_notice(request, id):
	pass
