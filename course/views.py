from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone

from student.models import Student
from .models import Course, CourseAssignment, CourseSyllabus, CourseLectureNotes, CourseNotice, CourseFeedback
from .forms import CourseAssignmentForm, CourseSyllabusForm, CourseLectureNotesForm, CourseNoticeForm, CourseFeedbackForm

from userauth.models import RegProfessor, RegStudent

def view_course(request, id):
	if request.user.is_authenticated():
		course = Course.objects.get(id=id)
		notices = CourseNotice.objects.filter(course=course)
		if RegStudent.objects.filter(user=request.user.id).exists():
			if RegStudent.objects.get(user=request.user).active:
				reg_student = RegStudent.objects.get(user=request.user)
				student = Student.objects.get(name=reg_student)
				if course in student.courses.all():
					return render_to_response("course/viewnotice.html", locals(), context_instance=RequestContext(request))
		elif RegProfessor.objects.filter(user=request.user.id).exists():
			if RegProfessor.objects.get(user=request.user).active:
				reg_professor = RegProfessor.objects.get(user=request.user)
				if course in Course.objects.filter(instructor=reg_professor):
					return render_to_response("course/viewnotice.html", locals(), context_instance=RequestContext(request))
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
			form = CourseAssignmentForm(request.POST or None, request.FILES or None)
			if form.is_valid():
				description = form.cleaned_data['description']
				assignment = form.cleaned_data['assignment']
				deadline = form.cleaned_data['deadline']
				CourseAssignment.objects.create(course=course, description=description, assignment=assignment, deadline=deadline, timestamp=timezone.now())
				messages.success(request, 'Your assignment was added')
				return HttpResponseRedirect(reverse('view_assignment', kwargs={'id': course.id})) 
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
	if request.user.is_authenticated() and RegProfessor.objects.get(user=request.user).active:
		reg_professor = RegProfessor.objects.get(user=request.user)
		course = Course.objects.get(id=id)
		if course.instructor == reg_professor:
			form = CourseSyllabusForm(request.POST or None, request.FILES or None)
			if form.is_valid():
				syllabus = form.cleaned_data['syllabus']
				CourseSyllabus.objects.create(course=course, syllabus=syllabus, timestamp=timezone.now())
				messages.success(request, 'Your syllabus was added!')
				return HttpResponseRedirect(reverse('view_syllabus', kwargs={'id': course.id}))
		return render_to_response("course/addsyllabus.html", locals(), context_instance=RequestContext(request))
	else:
		raise Http404

def view_lecture_notes(request, id):
	if request.user.is_authenticated():
		course = Course.objects.get(id=id)
		lecture_notes = CourseLectureNotes.objects.filter(course=course)
		if RegStudent.objects.filter(user=request.user.id).exists():
			if RegStudent.objects.get(user=request.user).active:
				reg_student = RegStudent.objects.get(user=request.user)
				student = Student.objects.get(name=reg_student)
				if course in student.courses.all():
					return render_to_response("course/viewlecturenotes.html", locals(), context_instance=RequestContext(request))
				else:
					raise Http404
		elif RegProfessor.objects.filter(user=request.user.id).exists():
			if RegProfessor.objects.get(user=request.user).active:
				reg_professor = RegProfessor.objects.get(user=request.user)
				if course in Course.objects.filter(instructor=reg_professor):
					return render_to_response("course/viewlecturenotes.html", locals(), context_instance=RequestContext(request))
				else:
					raise Http404
		else:
			raise Http404
	else:
		raise Http404

def add_lecture_notes(request, id):
	if request.user.is_authenticated() and RegProfessor.objects.get(user=request.user).active:
		reg_professor = RegProfessor.objects.get(user=request.user)
		course = Course.objects.get(id=id)
		if course.instructor == reg_professor:
			form = CourseLectureNotesForm(request.POST or None, request.FILES or None)
			if form.is_valid():
				lecture_notes = form.cleaned_data['lecture_notes']
				CourseLectureNotes.objects.create(course=course, lecture_notes=lecture_notes, timestamp=timezone.now())
				messages.success(request, 'Your Lecture Notes was added!')
				return HttpResponseRedirect(reverse('view_lecture_notes', kwargs={'id': course.id}))
		return render_to_response("course/addlecturenotes.html", locals(), context_instance=RequestContext(request))
	else:
		raise Http404

def add_notice(request, id):
	if request.user.is_authenticated() and RegProfessor.objects.get(user=request.user).active:
		reg_professor = RegProfessor.objects.get(user=request.user)
		course = Course.objects.get(id=id)
		if course.instructor == reg_professor:
			form = CourseNoticeForm(request.POST or None,)
			if form.is_valid():
				title = form.cleaned_data['title']
				content = form.cleaned_data['content']
				CourseNotice.objects.create(course=course, title=title, content=content ,timestamp=timezone.now())
				messages.success(request, 'Your notice was added!')
				return HttpResponseRedirect(reverse('view_course', kwargs={'id': course.id}))
		return render_to_response("course/addnotice.html", locals(), context_instance=RequestContext(request))
	else:
		raise Http404

def add_feedback(request, id):
	if request.user.is_authenticated() and RegStudent.objects.get(user=request.user).active:
		reg_student = RegStudent.objects.get(user=request.user)
		course = Course.objects.get(id=id)
		student = Student.objects.get(name=reg_student)
		if course in student.courses.all():
			form = CourseFeedbackForm(request.POST or None,)
			if form.is_valid():
				content = form.cleaned_data['content']
				CourseFeedback.objects.create(course=course, content=content ,timestamp=timezone.now())
				messages.success(request, 'Your feedback was recorded!')
				return HttpResponseRedirect(reverse('view_course', kwargs={'id': course.id}))
		return render_to_response("course/addfeedback.html", locals(), context_instance=RequestContext(request))
	else:
		raise Http404

def view_feedback(request, id):
	if request.user.is_authenticated():
		course = Course.objects.get(id=id)
		if RegProfessor.objects.filter(user=request.user.id).exists():
			if RegProfessor.objects.get(user=request.user).active:
				reg_professor = RegProfessor.objects.get(user=request.user)
				if course in Course.objects.filter(instructor=reg_professor):
					feedbacks = CourseFeedback.objects.filter(course=course)
					return render_to_response("course/viewfeedback.html", locals(), context_instance=RequestContext(request))
				else:
					raise Http404
		else:
			raise Http404
	else:
		raise Http404