from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.

def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    else:
        task_form = forms.TaskForm()
    return render(request, 'add_task.html', {'form' : task_form})

def complate_task(request, id):
    task = models.AddTask.objects.get(pk = id)
    task.is_completed = True
    task.save()
    return redirect('homepage')

def edit_task(request, id):
    task = models.AddTask.objects.get(pk = id)
    task_form = forms.TaskForm(instance = task)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance = task)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')

    return render(request, 'add_task.html', {'form' : task_form})



def delete_task(request, id):
    task = models.AddTask.objects.get(pk = id)
    task.delete()
    return redirect('homepage')