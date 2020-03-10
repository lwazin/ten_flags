from django.contrib import admin
from .models import UserType, Transaction, Item

# Register your models here.

admin.site.register(UserType)
admin.site.register(Transaction)
admin.site.register(Item)
