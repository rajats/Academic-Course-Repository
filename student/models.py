from django.db import models

from userauth.models import RegStudent
from course.models import Course 

class Student(models.Model):
	name = models.ForeignKey(RegStudent)
	courses = models.ManyToManyField(Course)
	

