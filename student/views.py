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
			reg_student = RegStudent.objects.get(user=request.user)
			student_sem = reg_student.semester
			student_programme = reg_student.programme
			student = Student.objects.get(name=reg_student)
		except RegStudent.DoesNotExist:
			student_sem = None
		try:
			print student_sem, student_programme
			courses = Course.objects.filter(semester=student_sem)
			unenrolled_compulsary_courses, unenrolled_elective1_courses, unenrolled_elective2_courses, unenrolled_elective3_courses = [],[],[],[]
			elective_one, elective_two, elective_three = False, False, False
			for course in student.courses.all():
				if student_sem == course.semester:
					if ('2' in course.course_type) and not elective_one:
						courses = Course.objects.filter(semester=student_sem).filter(~Q(course_type = '2'))
						elective_one = True
					if ('3' in course.course_type) and not elective_two:
						courses = Course.objects.filter(semester=student_sem).filter(~Q(course_type = '3'))
						elective_two = True
					if ('4' in course.course_type) and not elective_three:
						courses = Course.objects.filter(semester=student_sem).filter(~Q(course_type = '4'))
						elective_three = True
					if elective_one and elective_two:
						courses = Course.objects.filter(semester=student_sem).filter(~Q(course_type = '2')).filter(~Q(course_type = '3'))
					if elective_one and elective_two and elective_three:
						courses = Course.objects.filter(semester=student_sem).filter(~Q(course_type = '2')).filter(~Q(course_type = '3')).filter(~Q(course_type = '4'))
			for course in courses:
				if course not in student.courses.all() and student_programme in course.programme:
					if '1' in course.course_type:
						unenrolled_compulsary_courses.append(course)
					elif '2' in course.course_type:
						unenrolled_elective1_courses.append(course)
					elif '3' in course.course_type:
						unenrolled_elective2_courses.append(course)
					elif '4' in course.course_type:
						unenrolled_elective3_courses.append(course)
		except Course.DoesNotExist:
			courses = None
		return render_to_response("student/enroll.html", locals(), context_instance=RequestContext(request))
	else:
		messages.error(request, 'Your account is not active yet, please conatct admin.')
		return render_to_response("student/enroll.html", locals(), context_instance=RequestContext(request))

def my_courses(request):
	if request.user.is_authenticated() and RegStudent.objects.get(user=request.user).active:
		try:
			reg_student = RegStudent.objects.get(user=request.user)
		except RegStudent.DoesNotExist:
			reg_student = None
		try:
			student = Student.objects.get(name=reg_student)
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
		reg_student = RegStudent.objects.get(user=request.user)
		student = Student.objects.get(name=reg_student)
		student.courses.add(course)
		messages.success(request, 'You are enrolled in %s' %(course))
		return HttpResponseRedirect('/student/courses/')
	else:
		raise Http404


