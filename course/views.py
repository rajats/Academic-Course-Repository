from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone

from student.models import Student
from .models import Course, CourseAssignment, CourseSyllabus, CourseLectureNotes, CourseNotice, CourseFeedback, StudentAssignment, StudentAssignmentFeedback, StudentAssignmentFeedbackComments
from .forms import CourseAssignmentForm, CourseSyllabusForm, CourseLectureNotesForm, CourseNoticeForm, CourseFeedbackForm, StudentAssignmentForm, StudentAssignmentFeedbackFileForm, StudentAssignmentFeedbackTextForm, StudentAssignmentFeedbackCommentsForm

from userauth.models import RegProfessor, RegStudent

def verify_valid_student(request, id, course):
	"""
	Verifies that student accessing the course is enrolled in course
	"""
	if RegStudent.objects.filter(user=request.user.id).exists():
		if RegStudent.objects.get(user=request.user).active:
			reg_student = RegStudent.objects.get(user=request.user)
			student = Student.objects.get(name=reg_student)
			if course in student.courses.all():
				return [True, reg_student]
	return [False]

def verify_valid_professor(request, id, course):
	"""
	Verifies that professor accessing the course is instructor of course
	"""
	if RegProfessor.objects.filter(user=request.user.id).exists():
		if RegProfessor.objects.get(user=request.user).active:
			reg_professor = RegProfessor.objects.get(user=request.user)
			if course in Course.objects.filter(instructor=reg_professor):
				return [True, reg_professor]
	return [False]

def view_course(request, id):
	"""
	Shows course notice in course Layout.Course Notice is home page of a course
	"""
	if request.user.is_authenticated():
		course = Course.objects.get(id=id)
		notices = CourseNotice.objects.filter(course=course)
		valid_student = verify_valid_student(request, id, course)
		if valid_student[0]:
			reg_student = valid_student[1]
			return render_to_response("course/viewnotice.html", locals(), context_instance=RequestContext(request))
		valid_professor = verify_valid_professor(request, id, course)
		if valid_professor[0]:
			reg_professor = valid_professor[1]
			return render_to_response("course/viewnotice.html", locals(), context_instance=RequestContext(request))
		else:
			raise Http404
	else:
		raise Http404

def view_assignment(request, id):
	"""
	Shows course assignment in course Layout.If course instructor is viewing
	assignment then there is a button for adding assignment
	"""
	if request.user.is_authenticated():
		course = Course.objects.get(id=id)
		assignments = CourseAssignment.objects.filter(course=course)
		valid_student = verify_valid_student(request, id, course)
		if valid_student[0]:
			reg_student = valid_student[1]
			return render_to_response("course/viewassignment.html", locals(), context_instance=RequestContext(request))
		valid_professor = verify_valid_professor(request, id, course)
		if valid_professor[0]:
			reg_professor = valid_professor[1]
			return render_to_response("course/viewassignment.html", locals(), context_instance=RequestContext(request))
		else:
			raise Http404
	else:
		raise Http404

def add_assignment(request, id):
	"""
	Allows course instructor to add a course assignment
	"""
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
	"""
	Shows course Syllabus in course Layout.If course instructor is viewing
	syllabus then there is a button for adding syllabus
	"""
	if request.user.is_authenticated():
		course = Course.objects.get(id=id)
		syllabuses = CourseSyllabus.objects.filter(course=course)
		valid_student = verify_valid_student(request, id, course)
		if valid_student[0]:
			reg_student = valid_student[1]
			return render_to_response("course/viewsyllabus.html", locals(), context_instance=RequestContext(request))
		valid_professor = verify_valid_professor(request, id, course)
		if valid_professor[0]:
			reg_professor = valid_professor[1]
			return render_to_response("course/viewsyllabus.html", locals(), context_instance=RequestContext(request))
		else:
			raise Http404
	else:
		raise Http404

def add_syllabus(request, id):
	"""
	Allows course instructor to add course syllabus
	"""
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
	"""
	Shows course lecture notes in course Layout.If course instructor is viewing
	lecture notes then there is a button for adding lecture note
	"""
	if request.user.is_authenticated():
		course = Course.objects.get(id=id)
		lecture_notes = CourseLectureNotes.objects.filter(course=course)
		valid_student = verify_valid_student(request, id, course)
		if valid_student[0]:
			reg_student = valid_student[1]
			return render_to_response("course/viewlecturenotes.html", locals(), context_instance=RequestContext(request))
		valid_professor = verify_valid_professor(request, id, course)
		if valid_professor[0]:
			reg_professor = valid_professor[1]
			return render_to_response("course/viewlecturenotes.html", locals(), context_instance=RequestContext(request))
		else:
			raise Http404
	else:
		raise Http404

def add_lecture_notes(request, id):
	"""
	Allows course instructor to add lecture notes of course
	"""
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
	"""
	Allows course instructor to add course notice
	"""
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
	"""
	Allows student to give feedback for the course without revealing their identities
	"""
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
	"""
	Allows course instructor to view course feedback from students enrolled in course
	"""
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

def submit_assignment(request, c_id, a_id):
	"""
	Allows student to submit course assignment.Student can submit assignment multiple
	times before deadline.Only Last submission will be shown to the instructor
	"""
	if request.user.is_authenticated() and RegStudent.objects.get(user=request.user).active:
		reg_student = RegStudent.objects.get(user=request.user)
		course = Course.objects.get(id=c_id)
		course_assignment = CourseAssignment.objects.get(id=a_id)
		student = Student.objects.get(name=reg_student)
		submitted = False
		if StudentAssignment.objects.filter(student=reg_student.id).exists():
			submitted = True
			submitted_assignment = StudentAssignment.objects.get(student=reg_student)
		if course in student.courses.all():
			form = StudentAssignmentForm(request.POST or None, request.FILES or None)
			if form.is_valid():
				assignment = form.cleaned_data['assignment']
				if not submitted:
					StudentAssignment.objects.create(course=course, student=reg_student , course_assignment=course_assignment ,assignment=assignment ,timestamp=timezone.now())
				else:
					submitted_assignment.assignment = assignment
					submitted_assignment.timestamp = timezone.now()
					submitted_assignment.save()
				messages.success(request, 'Your assignment was submitted to the instructor!')
				return HttpResponseRedirect(reverse('view_assignment', kwargs={'id': course.id})) 
		return render_to_response("course/submitassignment.html", locals(), context_instance=RequestContext(request))
	else:
		raise Http404

def view_submitted_assignment(request, c_id, a_id):
	"""
	Allows course instructor to view submission of assignment from all students who 
	submitted assignment
	"""
	if request.user.is_authenticated():
		course = Course.objects.get(id=c_id)
		if RegProfessor.objects.filter(user=request.user.id).exists():
			if RegProfessor.objects.get(user=request.user).active:
				reg_professor = RegProfessor.objects.get(user=request.user)
				if course in Course.objects.filter(instructor=reg_professor):
					course_assignment = CourseAssignment.objects.get(id=a_id)
					submitted_assignments = StudentAssignment.objects.filter(course_assignment=course_assignment)
					return render_to_response("course/viewassignmentsubmissions.html", locals(), context_instance=RequestContext(request))
				else:
					raise Http404
		else:
			raise Http404
	else:
		raise Http404

def add_assignment_feedback(request, c_id , sa_id, form_type):
	"""
	Allows course instructor to give feedback to each submission of assignment.
	Feedback can be in form of file or as comment text
	"""
	if request.user.is_authenticated():
		course = Course.objects.get(id=c_id)
		if RegProfessor.objects.filter(user=request.user.id).exists():
			if RegProfessor.objects.get(user=request.user).active:
				reg_professor = RegProfessor.objects.get(user=request.user)
				if course in Course.objects.filter(instructor=reg_professor):
					student_assignment = StudentAssignment.objects.get(id=sa_id)
					student = student_assignment.student
					form_type = int (form_type)
					if form_type == 1:
						form = StudentAssignmentFeedbackFileForm(request.POST or None, request.FILES or None)
						if form.is_valid():
							file_feedback = form.cleaned_data['file_feedback']
							StudentAssignmentFeedback.objects.create(student_assignment=student_assignment,file_feedback=file_feedback, timestamp=timezone.now())
							messages.success(request, 'Your feedback was shared with the student!')
							return HttpResponseRedirect(reverse('view_assignment', kwargs={'id': course.id})) 
					elif form_type == 2:
						form = StudentAssignmentFeedbackTextForm(request.POST or None)
						if form.is_valid():
							text_feedback = form.cleaned_data['text_feedback']
							StudentAssignmentFeedback.objects.create(student_assignment=student_assignment,text_feedback=text_feedback, timestamp=timezone.now())
							messages.success(request, 'Your feedback was shared with the student!')
							return HttpResponseRedirect(reverse('view_assignment', kwargs={'id': course.id})) 
					return render_to_response("course/addassignmentfeedback.html", locals(), context_instance=RequestContext(request))
				else:
					raise Http404
		else:
			raise Http404
	else:
		raise Http404

def view_assignment_feedback(request, c_id, sa_id):
	"""
	Allows students and instructor to view feedback and discuss it in form of comment
	"""
	if request.user.is_authenticated():
		course = Course.objects.get(id=c_id)
		student_assignment = StudentAssignment.objects.get(id=sa_id)
		assignment_feedbacks = StudentAssignmentFeedback.objects.filter(student_assignment=student_assignment)
		comments = StudentAssignmentFeedbackComments.objects.filter(student_assignment=student_assignment)
		form = StudentAssignmentFeedbackCommentsForm()
		if RegStudent.objects.filter(user=request.user.id).exists():
			if RegStudent.objects.get(user=request.user).active:
				reg_student = RegStudent.objects.get(user=request.user)
				student = Student.objects.get(name=reg_student)
				if course in student.courses.all():
					if request.method=='POST':
						form=StudentAssignmentFeedbackCommentsForm(request.POST)
						if form.is_valid():
							comment_text = form.cleaned_data['comment']
							StudentAssignmentFeedbackComments.objects.create(student_assignment=student_assignment, commenter=request.user, comment=comment_text, timestamp=timezone.now())
							messages.success(request, "Your comment was added")
					return render_to_response("course/viewassignmentfeedback.html", locals(), context_instance=RequestContext(request))
				else:
					raise Http404
		elif RegProfessor.objects.filter(user=request.user.id).exists():
			if RegProfessor.objects.get(user=request.user).active:
				reg_professor = RegProfessor.objects.get(user=request.user)
				if course in Course.objects.filter(instructor=reg_professor):
					if request.method=='POST':
						form=StudentAssignmentFeedbackCommentsForm(request.POST)
						if form.is_valid():
							comment_text = form.cleaned_data['comment']
							StudentAssignmentFeedbackComments.objects.create(student_assignment=student_assignment, commenter=request.user, comment=comment_text, timestamp=timezone.now())
							messages.success(request, "Your comment was added")
					return render_to_response("course/viewassignmentfeedback.html", locals(), context_instance=RequestContext(request))
				else:
					raise Http404
		else:
			raise Http404
	else:
		raise Http404