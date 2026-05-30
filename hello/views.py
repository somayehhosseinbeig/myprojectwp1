from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"hello/index.html")

def somayeh(requset):
    return HttpResponse("Hello Somayeh")

def arnika(requset):
    return HttpResponse("Hello Arnika!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
