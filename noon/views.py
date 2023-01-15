from django.shortcuts import render
from django.http import HttpResponse
import datetime



def index(request):
    date = datetime.datetime.now()
    hour = int(date.strftime('%H'))
    name = 'asir'
    message = 'Hi '
    if hour<12:
        message+= ' Good Morning'
    else:
        message+= ' Good Evening'

    date_dict = {'display_date':hour, 'emp_name': name, 'display':message}
    return render(request,'noon/noon.html',context= date_dict)

def page1(request):
    return HttpResponse("Hello, you are in Page 1 <a href=/>Home </a> or <a href=/weblist>weblist </a> or <a href=/noon >Noon </a> ")

def page2(request):
    return HttpResponse("Hello, you are in Page 2 <a href=/>Home </a> or <a href=/weblist>weblist </a> or <a href=/noon >Noon </a> ")





# Create your views here.
