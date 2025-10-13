from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to LOMS - Learning Outcome Management System!")
