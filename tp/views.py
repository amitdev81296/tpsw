from django.shortcuts import render
from .models import UserLoginForm
from django.contrib.auth import authenticate
# Create your views here.


def index(request):
    return render(request, 'tp/index.html')


def login(request):
    form = UserLoginForm
    context = {'form': form}
    return render(request, 'tp/login.html', context)


def dashboard(request):
    form = UserLoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        # returns User objects if credentials are correct
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                return render(request, 'tp/dashboard.html', {'user': user})




