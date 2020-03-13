from django.shortcuts import render, redirect
from .models import Transaction, Item
from store.models import Temp, Store, User
import random
import string

# Create your views here.


def transaction(request):

    def ran_gen(size=6, chars=string.ascii_letters):
        x = ''.join(random.choice(chars) for x in range(size))
        if len(Transaction.objects.filter(transaction_id=x)) != 0:
            ran_gen()
        else:
            return x

    if request.method == 'POST':

        store_owner = Store.objects.get(
            store_id=request.POST['store']).store_owner.id

        if request.POST['confirmation'] == 'True':

            temp_transaction = Transaction()

            temp_transaction.transaction_buyer = request.user
            temp_transaction.transaction_store = Store.objects.get(
                store_id=request.POST['store'])
            temp_transaction.transaction_confirmation = request.POST['confirmation']
            # temp_transaction.transaction_date = ran_gen()
            temp_transaction.transaction_id = ran_gen()

            temp_transaction.save()

            for i in Temp.objects.filter(temp_store=store_owner):
                temp_item = Item()

                temp_item.item_transaction = temp_transaction
                temp_item.item_item = i.temp_item
                temp_item.item_quantity = i.temp_quantity

                temp_item.save()
                i.delete()

        elif request.POST['confirmation'] == 'False':
            print('Nooooooooooooo!')

    return redirect('receipt')
