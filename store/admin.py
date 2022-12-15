from django.contrib import admin
from store.models import Cart, Order, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)
