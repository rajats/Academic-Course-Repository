# encoding=utf8
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import CourseAssignment, CourseSyllabus, CourseLectureNotes


'''
class RegStudentForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(RegStudentForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			self.fields['enroll_no'].widget.attrs['readonly'] = True
			self.fields['programme'].widget.attrs['readonly'] = True
			self.fields['user'].widget.attrs['readonly'] = True

	class Meta:
		model = RegStudent
		fields = ('user','programme','enroll_no','semester')  
'''
