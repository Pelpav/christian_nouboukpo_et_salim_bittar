from django.shortcuts import render
from back.models import *
# Create your views here.
def home(request):
    return render(request, 'front/home.html')

def about(request):
    return render(request, 'front/about.html')

def contact(request):
    return render(request, 'front/contact.html')
def cars(request):
    return render(request, 'front/cars.html')

def services(request):
    return render(request, 'front/services.html')

def blog(request):
    return render(request, 'front/blog.html')

