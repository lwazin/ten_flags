from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Store(models.Model):
    store_name = models.CharField(max_length=64)
    store_owner = models.CharField(max_length=64)
    store_description = models.CharField(max_length=128)
    store_category = models.CharField(max_length=64)
    store_active = models.BooleanField(default=True)
    store_id = models.SlugField()


class Location(models.Model):
    location_store = models.OneToOneField(Store, on_delete=models.CASCADE)
    location_category = models.IntegerField(default=0)


class Item(models.Model):
    item_store = models.OneToOneField(Store, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=64)
    item_description = models.CharField(max_length=128)
    item_price = models.IntegerField(default=0)
    item_id = models.SlugField()
