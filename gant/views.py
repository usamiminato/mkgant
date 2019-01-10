from django.shortcuts import render

def task_list(request):
    return render(request, 'gant/task_list.html', {})
