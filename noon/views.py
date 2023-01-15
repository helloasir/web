from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, you are in noon click <a href=/>Home </a> or <a href=/weblist>weblist </a> or <a href=/noon >Noon </a> or <a href= page1 >Page1 </a> ")

def page1(request):
    return HttpResponse("Hello, you are in Page 1 <a href=/>Home </a> or <a href=/weblist>weblist </a> or <a href=/noon >Noon </a> ")

def page2(request):
    return HttpResponse("Hello, you are in Page 2 <a href=/>Home </a> or <a href=/weblist>weblist </a> or <a href=/noon >Noon </a> ")



# Create your views here.
