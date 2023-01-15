from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls.static import static



def index(request):
    return render(request,'main.html')   

# Create your views here.
