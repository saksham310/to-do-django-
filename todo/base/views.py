from django.shortcuts import render
from django.http import HttpResponse
from . models import Task
# Create your views here.
def taskList(request):
    context={}
    data=Task.objects.all()
    