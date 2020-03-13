from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from credit.models import Profile
from store.models import Store
from purchase.models import UserType
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect, HttpResponse
import random
import string
import pyqrcode
import os

# Create your views here.


def ran_gen(size=6, chars=string.ascii_letters):
    x = ''.join(random.choice(chars) for x in range(size))
    if len(Store.objects.filter(store_id=x)) != 0:
        ran_gen()
    else:
        return x


def landing_page(request):
    # if request.user is not None and request.user.is_authenticated:

    # user = User.objects.get(username=request.user)

    # user_type = UserType.objects.get(usertype_user=user.id).usertype_type

    # if user_type == 'store':
    #     return redirect('store')
    # elif user_type == 'customer':
    #     return redirect('customer')
    pass

    return render(request, 'index.html')


def logout(request):
    auth_logout(request)
    return redirect('landing_page')


def login(request):
    if request.method == 'POST':

        email = str(request.POST['email'])
        password = str(request.POST['password'])
        print(request.POST['email'])
        print(request.POST['password'])

        user = authenticate(username=email, password=password)

        print(user)
        if user is not None:
            if user.is_active:
                auth_login(request, user)

        return redirect('landing_page')

    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:

            signup_user = User()
            signup_user.email = request.POST['email']
            signup_user.first_name = request.POST['first_name']
            signup_user.last_name = request.POST['last_name']
            signup_user.set_password(request.POST['password'])
            signup_user.username = request.POST['email']
            signup_user.save()

            auth_login(request, signup_user)

            user_type = UserType()
            user_type.usertype_user = request.user
            user_type.usertype_type = request.POST['user_type']
            user_type.save()

            if user_type.usertype_type == 'store':

                temp_store = Store()
                temp_store.store_active = True
                temp_store.store_id = ran_gen()
                temp_store.store_owner = signup_user

                store_qr = pyqrcode.create(
                    'http://localhost:8000/store/'+temp_store.store_id)

                directory = 'media_root/user_'+str(signup_user.id)

                if not os.path.exists(directory):
                    os.makedirs(directory)

                store_qr.png('/media_root/user_' +
                             str(signup_user.id)+'/store_qr.png', scale=10)

                temp_store.store_qr = 'media_root/user_' + \
                    str(signup_user.id)+'/store_qr.png'
                temp_store.save()

    return render(request, 'index.html')
