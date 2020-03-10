from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from credit.models import Profile
from purchase.models import UserType
from django.contrib.auth import authenticate, login as auth_login, logout

# Create your views here.


def landing_page(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)
        auth_login(request, user)

        user_type = UserType.objects.get(usertype_user=user.id).usertype_type

        if user_type == 'store':
            return redirect('store')
        elif user_type == 'customer':
            return redirect('customer')

    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:

            signup_user = User()
            signup_user.email = request.POST['email']
            signup_user.first_name = request.POST['first_name']
            signup_user.last_name = request.POST['last_name']
            signup_user.password = request.POST['password']
            signup_user.username = request.POST['email']
            signup_user.save()

            auth_login(request, signup_user)

            user_type = UserType()
            user_type.usertype_user = request.user
            user_type.usertype_type = request.POST['user_type']
            user_type.save()

            print('Y O U   A R E   L O G G E D   I N !')

    return render(request, 'index.html')
