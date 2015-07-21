import datetime

from django.shortcuts import render, get_object_or_404
from django.utils.timezone import utc
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return HttpResponseRedirect('/task/tasks/')
    else:
        form = TaskForm()
    return render(request, 'task/addtask.html', {'form': form})

# @login_required
# def browse_by_name(request, initial=None):
#     if initial:
#         tasklist = Task.objects.filter(name__istartswith=initial)
#     else:
#         tasklist = Task.objects.all()   
#     return render(request, 'tasklist.html', {'tasklist': tasklist, 'initial':initial,})

@login_required
def task_list(request):
    if request.user.is_admin:
        tasklist = Task.objects.all()
    else:
        tasklist = Task.objects.filter(user=request.user)
    return render(request, 'tasklist.html', {'tasklist': tasklist, 'user':request.user})

@login_required
def delete_tasks(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return HttpResponseRedirect('/task/tasks/')

@login_required
def edit_task(request, pk):
    task_edit = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=task_edit)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task_edit)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/task/tasks/')
    
    return render(request, 'task/edittask.html', {'form': form, 'task': task_edit})

@login_required
def edit_in_place(request):
    task = get_object_or_404(Task, pk=request.POST.get('pk'))
    field_name = request.POST.get('name')
    field_value = request.POST.get('value')
    data = {field_name: field_value}
    form = TaskForm(data, instance=task)
    if form.is_valid():
        form.save()
    return HttpResponse()