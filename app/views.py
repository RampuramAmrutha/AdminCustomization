from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *


def insert_topic(request):
    ETMFO=TopicModelForm()
    d={'ETMFO':ETMFO}
    if request.method=='POST':
        TMFDO=TopicModelForm(request.POST)
        if TMFDO.is_valid():
            TMFDO.save()
            return HttpResponse('created')
        else:
            return HttpResponse('invalid ')
         
    return render(request,'insert_topic.html',d)
def insert_webpage(request):
    EWMFO=WebpageModelForm()
    d={'EWMFO':EWMFO}
    if request.method=='POST':
        WMFDO=WebpageModelForm(request.POST)
        if WMFDO.is_valid():
            WMFDO.save()
            return HttpResponse('created')
        else:
            return HttpResponse('invalid')
    return render(request,'insert_webpage.html',d)
def insert_accessrecord(request):
    EAMFO=AccessRecordModelForm()
    d={'EAMFO':EAMFO}
    if request.method=='POST':
        AMFDO=AccessRecordModelForm(request.POST)
        if AMFDO.is_valid():
            AMFDO.save()
            return HttpResponse('created')
        else:
            return HttpResponse('invalid')
    return render(request,'insert_accesrecord.html',d)
def wish(request,name):
    #return HttpResponse(f'Hello {name}! welcome to oursite')
    return HttpResponse('hello {} welcome to oursite'.format(name))