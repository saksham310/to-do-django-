from django.shortcuts import render
from django.http import HttpResponse
from . models import Task
# Create your views here.
def taskList(request):
    context={}
    data=Task.objects.all()
    context['data']=data
    return render(request,'base/task_list.html',context)