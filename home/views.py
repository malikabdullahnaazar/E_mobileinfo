from ast import Return
from multiprocessing import AuthenticationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import URLPattern,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
     # if not request.user.is_authenticated:
     #      return HttpResponseRedirect(reverse("login"))
     
        return render(request,"home/index.html")

def signup(request):
     return render(request,"home/signup.html")   
def signin(request):
     if request.method == "POST":
          username =request.POST["username"]
          password =request.POST["password"]
          user = authenticate(request,username=username,password=password)
          if user is not None:
               login(request,user)
               return HttpResponseRedirect(reverse("signin"))
          else:
               return render(request,"home/signin.html",{
                    "message":"Invalid credentials."
               })     
     return render(request,"home/signin.html")
  
def about(request):
     return render(request,"home/about.html")     