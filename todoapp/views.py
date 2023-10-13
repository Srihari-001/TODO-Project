from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todoapp/index.html', {'todos': todos})

def edit_task(request, task_id):
    task = Todo.objects.get(pk=task_id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=task)
    return render(request, 'todoapp/edit_task.html', {'form': form, 'task': task})
def add_task(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request, 'todoapp/add_task.html', {'form': form})