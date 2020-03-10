from django.shortcuts import render, redirect
from .models import Temp, Item
from django.contrib.auth.models import User


# Create your views here.


def store(request):

    temp_list = Temp.objects.filter(
        temp_store=User.objects.get(username=request.user))

    item_list = Item.objects.filter(
        item_store=User.objects.get(username=request.user))

    obj = {
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
