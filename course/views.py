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
	if request.user.is_authenticated() and RegStudent.objects.get(user=request.user).active:
		reg_student = RegStudent.objects.get(user=request.user)
		student = Student.objects.get(name=reg_student)
		course = Course.objects.get(id=id)
		if course in student.courses.all():
			return render_to_response("course/viewcourse.html", locals(), context_instance=RequestContext(request))
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
		return render_to_response("course/add_assignment.html", locals(), context_instance=RequestContext(request))
	else:
		raise Http404

def add_syllabus(request, id):
	pass

def add_lecture_notes(request, id):
	pass

def add_notice(request, id):
	pass
