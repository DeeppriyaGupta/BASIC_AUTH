from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def Register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, 'Username already taken!')
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email
        )

        user.set_password(password)
        user.save()
        return redirect('/login/')

    return render(request, 'register.html')


def Login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Username do not exist.')
            return redirect('/login/')
        
        #if user exists then authenticate return the object of user else it return None
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password.')
            return redirect('/login/')
        else:
            #login maintains the session
            login(request, user)
            return redirect('/home/')
        
    return render(request, 'login.html')


def Logout_page(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def Home_page(request):
    return render(request, 'index.html')