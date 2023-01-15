from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    message = 'this is <a href="/weblist"> weblist</a>'
    return HttpResponse(message)

# Create your views here.
