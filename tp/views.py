from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'tp/index.html')


def login(request):
    if request.method == 'POST':
        
    return render(request, 'tp/login.html')

