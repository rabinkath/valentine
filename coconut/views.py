from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>hello hi there<h1>")

def name(request):
    return HttpResponse("<h1>I am back!<h1>")