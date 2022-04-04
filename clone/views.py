from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.template import loader
from clone.forms import SignupForm
from django.contrib.auth.models import User

# Create your views here.
# def index(request):
#   template = loader.get_template('base.html')
#   return HttpResponse(template.render())


def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

def Signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			User.objects.create_user(username=username, email=email, password=password)
			return redirect('index')
	else:
		form = SignupForm()
	
	context = {
		'form':form,
	}

	return render(request, 'signup.html', context)