from django.db import models
from django.contrib.auth.models import User

from userauth.models import RegStudent
from course.models import Course 
from .signals import new_student_course 

class Student(models.Model):
	name = models.ForeignKey(RegStudent)
	courses = models.ManyToManyField(Course, null=True, blank=True)

def add_student_course(sender, **kwargs):
	kwargs.pop('signal', None)
	name = kwargs.pop('student')
	Student.objects.create(name=name)

new_student_course.connect(add_student_course)

#class StudentAssignment(models.Model):
#	student = models.ForeignKey(Student)
#	assignment = models.FileField(upload_to="studentassignments/files/")

