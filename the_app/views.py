from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass1']

        new_user = User.objects.create_user(username, email, password)
        new_user.save()

        user = authenticate(username = username, password = password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'timeline.html')


    return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'timeline.html')


    return render(request, 'signin.html')

def home(request):
    if request.user.is_authenticated:
        return render(request, 'timeline.html')
    else:    
        return render(request, 'welcome.html')

def Profile(request):
    if request.user.is_authenticated:
        name = 'undefined'
        username = request.user.username
        email = request.user.email
        
        context = {
            'name' : name,
            'username' : username,
            'email' : email,
        }

        return render(request, 'profile.html', context)
    else:    
        return render(request, 'welcome.html')
    

def signout(request):
    if request.user.is_authenticated:
        logout(request)
    
    return HttpResponse("Signout properly")

def dev_info(request):
    return render(request, 'dev_info.html')

