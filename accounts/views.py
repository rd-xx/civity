from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import redirect, render

User = get_user_model()

# Create your views here.
def signup(request):
	if request.method == "POST": 
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = User.objects.create_user(username=username, password=password)
		login(request, user)
		return redirect("index")
	
	return render(request, 'accounts/signup.html')

def signin(request):
	if request.method == "POST": 
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect("index")

	return render(request, 'accounts/signin.html')

def logout_user(request):
	logout(request)
	return redirect("index")