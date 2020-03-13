from django.db import models
from store.models import Store, Item as store_item
from django.contrib.auth.models import User


# Create your models here.


class UserType(models.Model):
    usertype_user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    usertype_type = models.SlugField(default='customer')


class Transaction(models.Model):
    transaction_buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    transaction_store = models.ForeignKey(
        Store, on_delete=models.CASCADE, null=True)
    transaction_confirmation = models.BooleanField(default=False)
    transaction_date = models.DateTimeField(auto_now_add=True, blank=True)
    transaction_id = models.SlugField()


class Item(models.Model):
    item_transaction = models.ForeignKey(
        Transaction, on_delete=models.CASCADE)
    item_item = models.ForeignKey(
        store_item, on_delete=models.CASCADE, null=True)
    item_quantity = models.IntegerField(default=1)
