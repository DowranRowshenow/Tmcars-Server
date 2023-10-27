from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Category, Location, Product

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Product)

admin.site.unregister(Group)
