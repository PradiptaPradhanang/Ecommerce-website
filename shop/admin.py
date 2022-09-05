from django.contrib import admin

from shop.views import contact

# Register your models here.

from .models import Contact, Product

admin.site.register(Product)
admin.site.register(Contact)
