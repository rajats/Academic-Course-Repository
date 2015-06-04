from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from .signals import new_student, new_professor

class RegStudent(models.Model):
	user = models.ForeignKey(User)
	branch = models.CharField(max_length=30)
	programme = models.CharField(max_length=2)
	enroll_no = models.IntegerField(validators=[MinValueValidator(100000),MaxValueValidator(199999)])    

class RegProfessor(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	branch = models.CharField(max_length=30)  


def reg_new_student(sender, **kwargs):
	kwargs.pop('signal', None)
	branch = kwargs.pop("branch")
	programme = kwargs.pop("programme")
	enroll_no = kwargs.pop("enroll_no")
	RegStudent.objects.create(user=sender, branch=branch, programme=programme, enroll_no=enroll_no)

new_student.connect(reg_new_student)

def reg_new_professor(sender, **kwargs):
	kwargs.pop('signal', None)
	branch = kwargs.pop("branch")
	RegProfessor.objects.create(user=sender, branch=branch)

new_professor.connect(reg_new_professor)

     
