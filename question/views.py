from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.models import CustomUser

# Create your views here.

def index(request):
    return render(request,'index.html')

def user_login(request):
    error=""
    if request.method=="POST":
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username = u, password = p)
        try:
            if user:
                login(request,user)
                error='no'
            else:
                error="yes"
        except:
            error="yes"
    d = {'error':error}

    return render(request,'user_login.html',d)

def signout(request):
    logout(request)
    return redirect('index')

def user_signup(request):
    error=""
    if request.method=="POST":
        f=request.POST['first_name']
        l=request.POST['last_name']
        e=request.POST['email']
        p=request.POST['phone']
        u=request.POST['username']
        p=request.POST['password']
        try:
            user = CustomUser.objects.create_user(username = u, password = p, first_name=f, last_name = l, email = e, phone = p)
            error="no"
        except:
            error="yes"
    return render(request, 'user_signup.html',{'error':error})

def user_index(request):
    return render(request, 'user_index.html')