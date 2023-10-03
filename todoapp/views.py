from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    if request.method == 'POST':
        new_todo = Todo(title=request.POST['title'])
        new_todo.save()
        return redirect('index')
    return render(request, 'index.html', {'todos': todos})
def complete_task(request, task_id):
    task = Todo.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect('index')
def delete_task(request, task_id):
    task = Todo.objects.get(pk=task_id)
    task.delete()
    return redirect('index')

from .forms import TodoForm

def add_task(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request, 'add_task.html', {'form': form})
