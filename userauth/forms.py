from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

User = get_user_model()

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)

class RegistrationFormStudent(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget = forms.PasswordInput)
	repeat_password = forms.CharField(widget = forms.PasswordInput)
	branch = forms.ChoiceField(choices=[(1,'Computer Science'),(2,'Information Technology')])
	programme = forms.ChoiceField(choices=[(1,'UG'),(2,'PG'),(3,'IPG')])
	enroll_no = forms.IntegerField()     

	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username = username).exists():
			raise forms.ValidationError("username %s already exists" %(username))
		return username

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email = email).exists():
			raise forms.ValidationError("email %s already exists" %(email))
		return email

	def clean(self):
		cleaned_data = super(RegistrationFormStudent,self).clean()
		password = cleaned_data.get("password")
		password1 = cleaned_data.get("repeat_password")
		if password != password1:
			raise forms.ValidationError("Passwords do not match")
			del cleaned_data['password']
			del cleaned_data['repeat_password']
		else:
			set_password = make_password(password)
			cleaned_data['password'] = set_password
			cleaned_data['repeat_password'] = set_password
		return cleaned_data

class RegistrationFormProfessor(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget = forms.PasswordInput)
	repeat_password = forms.CharField(widget = forms.PasswordInput)
	branch = forms.ChoiceField(choices=[(1,'Computer Science'),(2,'Information Technology')]) 

	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username = username).exists():
			raise forms.ValidationError("username %s already exists" %(username))
		return username

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email = email).exists():
			raise forms.ValidationError("email %s already exists" %(email))
		return email

	def clean(self):
		cleaned_data = super(RegistrationFormProfessor,self).clean()
		password = cleaned_data.get("password")
		password1 = cleaned_data.get("repeat_password")
		if password != password1:
			raise forms.ValidationError("Passwords do not match")
			del cleaned_data['password']
			del cleaned_data['repeat_password']
		else:
			set_password = make_password(password)
			cleaned_data['password'] = set_password
			cleaned_data['repeat_password'] = set_password
		return cleaned_data



