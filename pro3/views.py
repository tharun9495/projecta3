from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello")

def rend_demo(request):
    return render(request,"sample.html")
