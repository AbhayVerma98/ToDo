from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .models import *
from .forms import TodoForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages


def post(request):
    text = "hajj"
    return HttpResponse(text)


def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)
        if form.is_valid():
            form.save()
            todos = Todo.objects.all()
            messages.success(request, 'Task has been added')
            return render(request, "ToDo/home.html", {'todos': todos})
    else:
        todos = Todo.objects.all()
        return render(request, "ToDo/home.html", {'todos': todos})


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, 'Task has been Deleted!')
    return redirect('home')


def mark_complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('home')


def mark_incomplete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = False
    todo.save()
    return redirect('home')


def edit(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        form = TodoForm(request.POST or None, instance=todo)

        if form.is_valid():
            form.save()
            messages.success(request, ('Task has been edited!'))
            return redirect('home')
    else:
        todo = Todo.objects.get(id=todo_id)
        return render(request, 'ToDo/edit.html', {'todo': todo})

