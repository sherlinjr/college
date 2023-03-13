from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

def clg(request):
    return render(request,"index.html")


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,'new.html')
        else:
            messages.info(request,'invalid loging')
            return redirect('login')
    return render(request,"login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        conformpass = request.POST.get('conform password')
        if password == conformpass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, )
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password not matched")
        return redirect('register')
    return render(request, "register.html")


def form(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('form')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('form')

        myuser = User.objects.create_user(username, email )
        myuser.is_active = False
        myuser.save()
        messages.success(request,"Your order has been successfully placed !! ")
        return redirect('/')
    return render(request, 'form.html', {})

def logout(request):
    if  request.method=='POST':
        logout(request)
    return redirect('/')

def newpage(request):
    return  render(request,"new.html")