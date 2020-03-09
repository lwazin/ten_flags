from django.contrib.auth.models import User
from django.shortcuts import render
from credit.models import Profile
from store.models import Store
from django.contrib.auth import login, authenticate

# Create your views here.


def home(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        print('H E L L O   W O R L D')
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:

            signup_user = User()
            signup_user.email = request.POST['email']
            signup_user.first_name = request.POST['first_name']
            signup_user.last_name = request.POST['last_name']
            signup_user.password = request.POST['password']
            signup_user.save()

            login(request, signup_user)

            print('Y O U   A R E   L O G G E D   I N !')

    return render(request, 'index.html')
