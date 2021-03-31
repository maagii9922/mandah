from django.http import HttpResponse
from django.shortcuts import render
from .models import Person

def index(request):
    # return HttpResponse("hello")
    h=Person.objects.all()
    return render(request,'index.html',{'person':h})