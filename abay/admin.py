from django.contrib import admin
from .models import User, StoreAdmin, Customer, Product #Address
# Register your models here.

admin.site.register(StoreAdmin)
admin.site.register(Customer)
admin.site.register(Product)
# admin.site.register(Address)