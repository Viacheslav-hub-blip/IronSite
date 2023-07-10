from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def index(request):
    # tasks = Task.objects.all()
    #tasks = Task.objects.order_by('-id')
    #return render(request, 'mainPage/mainPage.html', {'title': 'Главная страница сайта', 'tasks': tasks})
    return render(request, 'mainPage/basePage.html')


def aboutUs(request):
    return render(request, 'mainPage/about-us.html')


def politics(request):
    return render(request, 'mainPage/politics.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'не верно'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainPage/create.html', context)
