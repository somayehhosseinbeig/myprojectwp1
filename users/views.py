from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request,"users/user.html")
    

def login_view(requset):
    if requset.method == "POST":
        username = requset.POST["username"]
        password = requset.POST["password"]
        user = authenticate(requset,username=username, password=password)
        if user is not None:
            login(requset,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(requset,"users/login.html",{
                "message":"Invalid credentials."
            })
    return render(requset,"users/login.html")

def logout_view(request):
    logout(request)
    return render(request,"users/login.html",{
        "message":"Logged Out."
    })
        
        
        
