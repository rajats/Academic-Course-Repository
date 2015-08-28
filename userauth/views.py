from django.shortcuts import render, render_to_response, HttpResponseRedirect, Http404, RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages

from student.signals import new_student_course
from .forms import LoginForm, RegistrationFormStudent, RegistrationFormProfessor, RegStudentForm
from .models import RegStudent, RegProfessor
from .signals import new_student, new_professor

User = get_user_model()

def signin(request):
	"""
	Allows registered users to sign in 
	"""
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('home'))
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			login(request, user)
			if RegStudent.objects.filter(user=user).exists():
				reg_student = RegStudent.objects.get(user=user)
			elif RegProfessor.objects.filter(user=user).exists():
				reg_professor = RegProfessor.objects.get(user=user)
			return render(request, "home.html", locals())
		else:
			messages.error(request, 'username or password does not match')
	context = {'form': form}
	return render(request, "userauth/loginform.html",context)


def register_student(request):
	"""
	Allows a new student to register themselves with restrictions
	in registration form to a particular college. All acount will remain
	inactive until admin activates it
	"""
	form = RegistrationFormStudent(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		programme = form.cleaned_data['programme']
		enroll_no = form.cleaned_data['enroll_no']
		semester = form.cleaned_data['semester']
		new_user, created = User.objects.get_or_create(username = username, email = email)
		if created:
			new_user.password = password
			new_user.save()
			new_student.send(new_user, programme=programme, enroll_no=enroll_no, semester=semester)
			student = RegStudent.objects.get(user=new_user)
			new_student_course.send(new_user,student=student)
			messages.success(request, 'Your account has been registered!')
			return HttpResponseRedirect('/userauth/login/')
	context = {'form': form}
	return render(request, "userauth/regform.html",context)

def register_professor(request):
	"""
	Allows new professor to register themselves.Account will been
	activated by admin after verifying details
	"""
	form = RegistrationFormProfessor(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		new_user, created = User.objects.get_or_create(username = username, email = email)
		if created:
			new_user.password = password
			new_user.save()
			new_professor.send(new_user)
			messages.success(request, 'Your account has been registered!')
			return HttpResponseRedirect('/userauth/login/')
	context = {'form': form}
	return render(request, "userauth/regform.html",context)

def signout(request):
	"""
	Allows registered users to sign out from site
	"""
	logout(request)
	messages.success(request,"You have logged out")
	return HttpResponseRedirect('/userauth/login/')

def account_info(request):
	"""
	Shows the account information of a student with all fields disabled
	except semester which is only for testing purpose
	"""
	if request.user.is_authenticated() and RegStudent.objects.get(user=request.user).active:
		try:
			reg_student = RegStudent.objects.get(user=request.user)
		except RegStudent.DoesNotExist:
			reg_student = None
		form = RegStudentForm(request.POST or None, instance=reg_student)
		if form.is_valid():
			account_edit = form.save(commit=False)
			account_edit.save()
		return render_to_response("userauth/account.html", locals(), context_instance=RequestContext(request))
	else:
		raise Http404

