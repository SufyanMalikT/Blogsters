from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.

def v_sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('blog_home')
    else:
        form = UserCreationForm()
    return render(request,'accounts/sign_up.html',{'form':form})

def v_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('blog_home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request,'accounts/log_in.html',{})

def v_logout(request):
    logout(request)
    return redirect('blog_home')


