from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.filter().order_by('to_be_complete_date')
    return render(request, 'gant/task_list.html', {'tasks':tasks})

def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_list')
    form = TaskForm()
    return render(request, 'gant/task_edit.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_list')
    form = TaskForm(instance=task)
    return render(request, 'gant/task_edit.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')
