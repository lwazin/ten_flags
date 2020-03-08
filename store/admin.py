from django.contrib import admin
from .models import Store, Location, Item

# Register your models here.

admin.site.register(Store)
admin.site.register(Location)
admin.site.register(Item)
