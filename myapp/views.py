from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Narawit MiniProject</h1>")

def about(request):
    return HttpResponse("About Me")

def form(request):
    return HttpResponse("Form")