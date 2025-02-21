from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("This is the home page")    # This is a simple HttpResponse