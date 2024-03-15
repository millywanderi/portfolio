from django.shortcuts import render, redirect
from django.contrib.auth.models import User
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
                return redirect("register")  #  redirect to login once login url is created
        else: 
            messages.error(request, f'password not matching')
            return redirect('register')
    return render(request, 'accounts/register.html')
