# encoding=utf8
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

from course.models import Course 

'''
class StudentCourseForm(ModelForm):
	class Meta:
		model = Course
		fields = ('name')


	def __init__(self, user=None, **kwargs):
        super(StudentCourseForm, self).__init__(**kwargs)
        sem = kwargs.pop('semester')
        if user:
            self.fields['name'].queryset = models.Course.objects.filter(semester=sem)
'''
	


