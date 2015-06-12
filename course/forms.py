# encoding=utf8
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Course, CourseAssignment, CourseSyllabus, CourseLectureNotes, CourseNotice

class CourseAssignmentForm(ModelForm):
	class Meta:
		model = CourseAssignment
		fields = ('description','assignment','deadline')  

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
		fields = ('content',)  
