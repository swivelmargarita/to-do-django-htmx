from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from .forms import TaskForm
from .models import Task


@require_GET
def index(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks,
    }
    return render(request, "toDoApp/index.html", context=context)

@require_GET
def view_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {
        "task": task,
    }
    return render(request, "toDoApp/task.html", context=context)
    
@require_http_methods(["GET", "POST"])
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = TaskForm()
    context = {
            "form": form
            }
    return render(request, "toDoApp/create.html", context=context)

def delete_task(request, pk):
    if request.POST:
        Task.objects.get(pk=pk).delete()
    return redirect("index")

@require_http_methods(["GET", "POST"])
def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = TaskForm(instance=task)
    context = {
            "task": task,
            "form": form,
            }
    return render(request, "toDoApp/editform.html", context=context)
