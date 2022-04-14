from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout

from accounts.forms import RegistrationForm
from api.views import *



def register_view(request,*args,**kwargs):
	user=request.user
	if user.is_authenticated:
		return redirect("home")
	context={}
	if request.POST:
		form =RegistrationForm(request.POST)
		if form.is_valid():
			
			form.save()
			email=form.cleaned_data.get('email').lower()
			raw_password=form.cleaned_data.get('password1')
			account=authenticate(email=email,password=raw_password)
			
			# otpverification(request.POST)
			login(request,account)
			destination=get_redirect_if_exists(request)
			if destination:
				return redirect(destination)
			return redirect("home")

		else:
			context['registration_form']=form



	return render(request,'account/register.html',context)

def home(request):
	user=request.user
	if user.is_authenticated:
		return HttpResponse(f'you are alreday authenticate as {user.email}.')
	else:
		return redirect("register")
def logout_view(request):
	logout(request)
	return redirect("home")

def login(request):
	context={}
	if user.is_authenticated:
		return redirect("home")
	destination=get_redirect_if_exists(request)
	if request.POST:
		form=Accountauthentication(request.POST)
		if form.is_valid:
			email=request.POST['email']
			password=request.POST['password1']
			user=authenticate(email=email,password=password)


	return render(request,'account/login.html')



def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect


