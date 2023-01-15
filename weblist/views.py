from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the weblist.click here to go <a href=/>Home </a>")

# Create your views here.
