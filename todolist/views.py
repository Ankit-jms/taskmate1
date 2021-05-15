from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist.models import tasklist
from todolist.forms import taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def todolist(request):
    if request.method =="POST":
        form=taskform(request.POST or None)
        if form.is_valid():
            form.save(commit=False).manage = request.user
            form.save()
        messages.success(request,("New Task Added!"))    
        return redirect('todolist')    
    else:
        all_task = tasklist.objects.filter(manage=request.user)
        paginator=Paginator(all_task,5)
        page=request.GET.get('pg')
        all_task=paginator.get_page(page)
   
        return render(request,'todo.html' ,{'all_task':all_task})
def contact(request):
    context = {
        'contact_text':"welcome to contact page.",
    }
    return render(request,'contact.html' ,context)
def about(request):
    context = {
        'about_text':"welcome to about page",
    }
    return render(request,'about.html' ,context)
def home(request):
    context = {
        'home_text':"Welcome to our home page",
        
    }
    return render(request,'home.html' ,context) 
@login_required    
def delete_task(request,task_id):
    task=tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request,("ACCESS Denied,SORRY!"))    
    messages.success(request,("Task deleted Successfully!"))
    return redirect('todolist')
@login_required    
def edit_task(request,task_id):
    if request.method =="POST":
        task=tasklist.objects.get(pk=task_id)
        form = taskform(request.POST or None,instance=task)
        if form.is_valid():
            form.save(commit=False).manage=request.user
            form.save()


        
        messages.success(request,("Task edited Successfully!"))    
        return redirect('todolist')    
    else:
        task_obj = tasklist.objects.get(pk=task_id)

   
        return render(request,'edit.html' ,{'task_obj':task_obj})
@login_required        
def complete_task(request,task_id):
    task=tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done=True
        task.save()
    else:
         messages.error(request,("ACCESS Denied,SORRY!"))

    messages.success(request,("Task completed Successfully!"))
    return redirect('todolist')
@login_required    
def pending_task(request,task_id):
    task=tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done=False
        task.save()
    else:
        messages.error(request,("ACCESS Denied,SORRY!"))

    messages.success(request,("Task pending See carefully!"))
    return redirect('todolist')                  



