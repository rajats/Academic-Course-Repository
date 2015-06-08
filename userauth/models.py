from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from .signals import new_student, new_professor

class RegStudent(models.Model):
	user = models.ForeignKey(User)
	programme = models.CharField(max_length=50)
	enroll_no = models.CharField(max_length=50)
	semester = models.IntegerField(default=1)   
	active = models.BooleanField(default=False)

	def __unicode__(self):
		return str(self.user)

class RegProfessor(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	active = models.BooleanField(default=False)

	def __unicode__(self):
		return str(self.user)


def reg_new_student(sender, **kwargs):
	kwargs.pop('signal', None)
	programme = kwargs.pop("programme")
	enroll_no = kwargs.pop("enroll_no")
	semester = kwargs.pop("semester")
	RegStudent.objects.create(user=sender, programme=programme, enroll_no=enroll_no, semester=semester)

new_student.connect(reg_new_student)

def reg_new_professor(sender, **kwargs):
	kwargs.pop('signal', None)
	RegProfessor.objects.create(user=sender)

new_professor.connect(reg_new_professor)

     
