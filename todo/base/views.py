from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Task
from . forms import TaskForm
# Create your views here.
def taskList(request):
    context={}
    data=Task.objects.all()
    form=TaskForm()
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
            
    context['data']=data
    context['form']=form
    return render(request,'base/task_list.html',context)

def taskUpdate(request,pk):
    obj=Task.objects.get(id=pk)
    context={}
    form=TaskForm(instance=obj)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/")
    context['form']=form
    return render(request,'base/task_update.html',context)
