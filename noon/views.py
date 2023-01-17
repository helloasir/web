from django.shortcuts import render
from django.http import HttpResponse
import datetime
from noon.models import Web
from . import views




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


def web(request):
    webdata = Web.objects.all()
    context = {'webdata': webdata}
    return render(request,'noon/web.html',context)





# Create your views here.
