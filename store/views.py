from django.shortcuts import render, redirect
from .models import Temp, Item, Store
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
import random
import string
import pyqrcode


# Create your views here.

def store(request, slug):

    temp_list = Temp.objects.filter(
        temp_store=Store.objects.get(store_id=slug))

    print(request.user)

    item_list = Item.objects.filter(
        item_store=Store.objects.get(store_id=slug))

    obj = {
        'store': Store.objects.get(store_id=slug),
        'temp_list': temp_list,
        'item_list': item_list
    }

    return render(request, 'authentication/store.html', obj)


def customer(request):
    return render(request, 'authentication/customer.html')


def add_item(request):

    if request.method == 'POST':

        temp = Temp()
        temp.temp_store = request.user
        temp.temp_item = Item.objects.get(item_id=request.POST['product'])
        temp.temp_quantity = request.POST['quantity']
        temp.temp_total = int(temp.temp_item.item_price) * \
            int(request.POST['quantity'])
        temp.save()

    return redirect('store')


def delete_item(request):

    if request.method == 'POST':
        item = Item.objects.get(item_id=request.POST['product'])
        temp = Temp.objects.get(temp_item=item)
        temp.delete()

    return redirect('store')


def create_item(request):

    def ran_gen(size=6, chars=string.ascii_letters):
        x = ''.join(random.choice(chars) for x in range(size))
        if len(Item.objects.filter(item_id=x)) != 0:
            ran_gen()
        else:
            return x

    if request.method == 'POST':

        item = Item()
        item.item_store = Store.objects.get(store_owner=request.user)
        item.item_name = request.POST['name']
        item.item_description = request.POST['description']
        item.item_price = request.POST['price']
        item.item_picture = request.FILES['image']
        item.item_id = ran_gen()

        item.save()

    return redirect('store')


def generate_qrcode(request):
    store_qr = pyqrcode.create('http://localhost:8000/receipt')
    store_qr.png('media_root/user_' +
                 str(User.objects.get(username=request.user).id)+'/store_qr.png', scale=10)
    return redirect('store')


def receipt(request):

    store_owner = User.objects.get(username=request.user).id
    if len(Temp.objects.filter(temp_store=store_owner)) < 1:
        return redirect('store')

    receipt = Temp.objects.filter(temp_store=request.user)
    obj = {
        'receipt': receipt
    }
    return render(request, 'store/receipt.html', obj)
