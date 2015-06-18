# encoding=utf8
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget

from .models import Course, CourseAssignment, CourseSyllabus, CourseLectureNotes, CourseNotice, CourseFeedback, StudentAssignment

class CourseAssignmentForm(forms.Form):
	description = forms.CharField()
	assignment = forms.FileField()
	deadline = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))

class CourseSyllabusForm(ModelForm):
	class Meta:
		model = CourseSyllabus
		fields = ('syllabus',)  

class CourseLectureNotesForm(ModelForm):
	class Meta:
		model = CourseLectureNotes
		fields = ('lecture_notes',)  

class CourseNoticeForm(ModelForm):
	class Meta:
		model = CourseNotice
		fields = ('title','content',)  

class CourseFeedbackForm(ModelForm):
	class Meta:
		model = CourseFeedback
		fields = ('content',) 

class StudentAssignmentForm(ModelForm):
	class Meta:
		model = StudentAssignment 
		fields = ('assignment',)

		
