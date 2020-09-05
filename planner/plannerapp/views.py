from django.shortcuts import render
from django.utils import timezone
import datetime
from .models import Task, TaskForm
from django.http import HttpResponseRedirect, HttpResponse
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, AnonymousUser
from django.urls import reverse


def auth_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    user.last_login = timezone.now()
                    return HttpResponseRedirect(reverse('main_tasks'))
        else:
            return render(request, 'plannerapp/login.html', {'login_form': form })
    form = AuthenticationForm()
    return render(request, 'plannerapp/login.html', {'login_form': form })


def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            return HttpResponseRedirect(reverse('main_tasks'))
    else:
        form = UserCreationForm()
    return render(request, 'plannerapp/signup.html', {'create_form': form})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()  
            return HttpResponseRedirect(reverse('main_tasks')) 
    form = TaskForm()
    return render(request, 'plannerapp/addtask.html', {'add_form': form})


def check_task(request):
    if request.method == 'POST':
        checklist = request.POST.getlist('checkedbox')
        for i in range(len(checklist)):
            tasks = Task.objects.filter(id = int(checklist[i]))
        for i in tasks:
            i.status = True
    return render(request, 'plannerapp/tasks.html', {'check_form': form})


def main_tasks(request):
    user = request.user
    if user.is_authenticated:  
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        today_tasks = Task.objects.filter(date=today, user=user)
        tomorrow_tasks = Task.objects.filter(date=tomorrow, user=user)
        week_tasks = Task.objects.filter(date__range = [tomorrow, tomorrow + datetime.timedelta(days=7)], user=user)
        return render(request, 'plannerapp/tasks.html', {
            'tasks': today_tasks, 
            'tomorrow_tasks': tomorrow_tasks, 
            'week_tasks': week_tasks,
            'user': user
            })
    else:
        return HttpResponse('error')


def tasks_atdate(request):
    """if request.method == 'GET':
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            task_date = form.save(commit=False) 
            task_date.save()
        else:
            search_form = SearchForm()"""
    #if request.GET.get('tomorrow', '') != None:
    date_tasks = Task.objects.filter(date=datetime.date.today() + datetime.timedelta(days=1))
    return render(request, 'plannerapp/tomorrow_tasks.html', {'date_tasks': date_tasks})








