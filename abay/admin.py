from django.contrib import admin
from .models import User, StoreAdmin, Customer, Product, Order, Comment, Cart, ProductInCart #Reviews #Address
# Register your models here.

admin.site.register(StoreAdmin)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Cart)
admin.site.register(ProductInCart)
# admin.site.register(Reviews)

# admin.site.register(Address)