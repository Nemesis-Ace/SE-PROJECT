from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms



# Create your views here.
def index(request):
    return render(request,'index.html',context=None)
