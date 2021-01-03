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


'''
def master(request):
    return render(request, "master.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def login(request):
    return render(request, "login.html")

def logout(request):
    return render(request, "logout.html")

def index(request):
    return render(request,'index.html')


def Registration(request):
    if request.method=='POST':
        form = Reg_Form(request.POST)
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if form.is_valid():
            form.save()
            return render(request, "home.html")

    else:
        form = Reg_Form()
    return render(request, "Registration.html",{'form':form})

def details(request):
    if request.method=='POST':
        form = Details_Form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = Details_Form()
    return render(request, "detail form.html",{'form':form})

def show_details(request):
    details = Details.objects.all()
    return render(request,'Details.html',{'details':details})

def search(request):
    user_list = Details.objects.all()
    user_filter = DetailsFilter(request.GET, queryset=user_list)
    return render(request, 'search.html', {'filter': user_filter})
    
    '''

