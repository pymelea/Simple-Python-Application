from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def signup(request):
    return HttpResponse("This is the signup page!")

def signin(request):
    return HttpResponse("This is the signin page!")

def home(request):
    return render(request, 'welcome.html')

def Profile(request):
    return HttpResponse("This is the profile page!")

def signout(request):
    return HttpResponse("This is the signout page!")

