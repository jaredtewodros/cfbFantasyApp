from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'fantasyApp/index.html', {})

def login(request):
    return render(request, 'fantasyApp/login.html', {})