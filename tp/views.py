from django.shortcuts import render
from .models import UserLoginForm, UserProfile
from django.contrib.auth import authenticate
# Create your views here.


def index(request):
    return render(request, 'tp/index.html')


def login(request):
    form = UserLoginForm()
    context = {'form': form}
    return render(request, 'tp/login.html', context)


def dashboard(request):
    if request.method == 'POST':
        empty_form = UserLoginForm()
        un = request.POST['username']
        pw = request.POST['password']
        user = authenticate(username=un, password=pw)
        user_profile = UserProfile.objects.get(user = user)
        if user:
            return render(request, 'tp/dashboard.html', {'user': user, 'user_profile': user_profile})
        else:
            return render(request, 'tp/login.html', {'form': empty_form})

