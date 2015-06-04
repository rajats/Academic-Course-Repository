from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages

from .forms import LoginForm, RegistrationFormStudent, RegistrationFormProfessor
from .signals import new_student, new_professor

User = get_user_model()

def signin(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			login(request, user)
			#return HttpResponseRedirect('//')
			return render_to_response("home.html", locals(), context_instance=RequestContext(request))
		else:
			messages.error(request, 'username or password does not match')
	context = {'form': form}
	return render(request, "userauth/loginform.html",context)


def register_student(request):
	form = RegistrationFormStudent(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		branch = form.cleaned_data['branch']
		programme = form.cleaned_data['programme']
		enroll_no = form.cleaned_data['enroll_no']
		new_user, created = User.objects.get_or_create(username = username, email = email)
		if created:
			new_user.password = password
			new_user.save()
			new_student.send(new_user, branch=branch, programme=programme, enroll_no=enroll_no)
			messages.success(request, 'Your account has been registered!')
			return HttpResponseRedirect('/userauth/login/')
	context = {'form': form}
	return render(request, "userauth/regform.html",context)

def register_professor(request):
	form = RegistrationFormProfessor(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		branch = form.cleaned_data['branch']
		new_user, created = User.objects.get_or_create(username = username, email = email)
		if created:
			new_user.password = password
			new_user.save()
			new_student.send(new_user, branch=branch)
			messages.success(request, 'Your account has been registered!')
			return HttpResponseRedirect('/userauth/login/')
	context = {'form': form}
	return render(request, "userauth/regform.html",context)

def signout(request):
	logout(request)
	messages.success(request,"You have logged out")
	return HttpResponseRedirect('/userauth/login/')

