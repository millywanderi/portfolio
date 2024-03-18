from django.shortcuts import render

# Create your views here.

def home(request):
    """Function that displays the application homepage"""
    return render(request, 'homepage/home.html')

def about(request):
    """View that offeors the application decsiption"""
    return render(request, 'homepage/about.html')

def contact(request):
    """Provides contact information"""
    return render(request, 'homepage/contact.html')
