from django.db import models
from store.models import Store
from django.contrib.auth.models import User


# Create your models here.


class UserType(models.Model):
    usertype_user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    usertype_type = models.SlugField(default='customer')


class Transaction(models.Model):
    transaction_buyer = models.OneToOneField(
        User, on_delete=models.CASCADE)
    transaction_store = models.OneToOneField(
        Store, on_delete=models.CASCADE)
    transaction_confirmation = models.BooleanField(default=False)
    transaction_date = models.DateTimeField(auto_now_add=True, blank=True)
    transaction_id = models.SlugField()


class Item(models.Model):
    item_transaction = models.OneToOneField(
        Transaction, on_delete=models.CASCADE)
    item_quantity = models.IntegerField(default=1)
