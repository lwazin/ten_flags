from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id> / <filename>
    return 'user_{0}/{1}'.format(instance.item_store.id, filename)


class Store(models.Model):

    store_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=64)
    store_description = models.CharField(max_length=128)
    store_category = models.CharField(max_length=64)
    store_active = models.BooleanField(default=True)
    store_id = models.SlugField()
    store_qr = models.CharField(null=True, max_length=64)


class Location(models.Model):
    location_store = models.ForeignKey(User, on_delete=models.CASCADE)
    location_category = models.IntegerField(default=0)


class Item(models.Model):
    item_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=64)
    item_description = models.CharField(max_length=128)
    item_price = models.IntegerField(default=0)
    item_picture = models.ImageField(
        upload_to=user_directory_path, default=None, null=True)
    item_id = models.SlugField()


class Temp(models.Model):
    temp_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    temp_item = models.OneToOneField(Item, on_delete=models.CASCADE)
    temp_quantity = models.IntegerField(default=None)
    temp_total = models.IntegerField(default=None, null=True)
