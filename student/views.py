from django.shortcuts import render_to_response, RequestContext, Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q 

from course.models import Course 
from userauth.models import RegStudent
from .models import Student

def show_courses(request):
	if request.user.is_authenticated() and RegStudent.objects.get(user=request.user).active:
		try:
			instance = RegStudent.objects.get(user=request.user)
			student_sem = instance.semester
			student_programme = instance.programme
			student = Student.objects.get(name=instance)
		except RegStudent.DoesNotExist:
			student_sem = None
		try:
			courses = Course.objects.filter(semester=student_sem).filter(programme=student_programme)
			unenrolled_courses = []
			elective_one, elective_two, elective_three = False, False, False
			for course in student.courses.all():
				if ('2' in course.course_type) and not elective_one:
					courses = Course.objects.filter(semester=student_sem).filter(programme=student_programme).filter(~Q(course_type = '2'))
					elective_one = True
				elif ('3' in course.course_type) and not elective_two:
					courses = Course.objects.filter(semester=student_sem).filter(programme=student_programme).filter(~Q(course_type = '3'))
					elective_two = True
				elif ('4' in course.course_type) and not elective_three:
					courses = Course.objects.filter(semester=student_sem).filter(programme=student_programme).filter(~Q(course_type = '4'))
					elective_three = True
			for course in courses:
				if course not in student.courses.all():
					unenrolled_courses.append(course)
		except Course.DoesNotExist:
			courses = None
		return render_to_response("student/enroll.html", locals(), context_instance=RequestContext(request))
	else:
		messages.error(request, 'Your account is not active yet, please conatct admin.')
		return render_to_response("student/enroll.html", locals(), context_instance=RequestContext(request))

def my_courses(request):
	if request.user.is_authenticated() and RegStudent.objects.get(user=request.user).active:
		try:
			name = RegStudent.objects.get(user=request.user)
		except RegStudent.DoesNotExist:
			name = None
		try:
			student = Student.objects.get(name=name)
		except Student.DoesNotExist:
			student = None
		my_enrolled_courses = student.courses.all()
		return render_to_response("student/mycourses.html", locals(), context_instance=RequestContext(request))
	else:
		messages.error(request, 'Your account is not active yet, please conatct admin.')
		return render_to_response("student/mycourses.html", locals(), context_instance=RequestContext(request))



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

