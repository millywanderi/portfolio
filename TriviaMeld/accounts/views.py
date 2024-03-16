from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def register(request):
    """Registers the user to access the trivia"""
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, f'email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.error(request, f'usename already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                                username=username, password=password1)
                user.save()
                return redirect("login")
        else: 
            messages.error(request, f'password not matching')
            return redirect('register')
    return render(request, 'accounts/register.html')

def login(request):
    """Login the user after registration"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('register') # Change to trivia homepage once created
        else:
            messages.error(request, f'Invalid username or password')
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout(request):
    """Logout the user"""
    auth.logout(request)
    return redirect('login')
