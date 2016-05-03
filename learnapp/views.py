# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.
from django import forms
def views(request):
    a = '速度与基情'
    return render_to_response('index.html',{'demoa':a})

class Userform(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()


def register(request):
    if request.method=="POST":
        uf = Userform(request.POST,request.FILES)
        if uf.is_valid():
            return HttpResponse('upload ok')
    else:
        uf = Userform()

    return render_to_response('Files.html',{'uf':uf})