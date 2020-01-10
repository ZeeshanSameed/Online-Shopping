from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User


class User(AbstractUser):
    is_store_admin = models.BooleanField('store status', default=False)
    is_customer = models.BooleanField('customer status', default=False)


class StoreAdmin(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=200)
    #avatar = models.ImageField()
    # location = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

# '''@receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Store_admin.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.Store_admin.save()
# '''


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=200)
    #avatar = models.ImageField()
    # location = models.CharField(max_length=50, blank=True)


# class Address(models.Model):
#     country = models.CharField(max_length=10)
#     city = models.CharField(max_length=20)
#     zipcode = models.IntegerField()
#     shipping_address = models.CharField(max_length=40)
#     billing_address = models.CharField(max_length=40)
#     customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
#     storeadmin = models.ForeignKey(
#         StoreAdmin, null=True, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=5000)
    price = models.IntegerField()
    saleprice = models.IntegerField()
    storeadmin = models.ForeignKey(
        StoreAdmin, null=True, on_delete=models.CASCADE)

    def soft_delete(self):
        self.is_deleted = True
        # self.deleted_at = timezone.now()
        self.save()


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total = models.IntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)
    shipping_address = models.CharField(max_length=30, default='')
    billing_address = models.CharField(max_length=30, default='')
    

class Cart(models.Model):
    customer = models.OneToOneField(
        Customer, null=True, on_delete=models.CASCADE)
    # quantity = models.IntegerField(null=True, blank=True,default=0)


class ProductInCart(models.Model):
    cart = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, default='')
    quantity = models.IntegerField(null=True, blank=True, default=0)

    # class Reviews(models.Model):
    #     customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    #     product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    #     body = models.CharField(max_length=100)
    #     rating = models.IntegerField(choices=Rating_CHOICES, default=1)
    # Rating_CHOICES = (
    #     (1, 'Poor'),
    #     (2, 'Average'),
    #     (3, 'Good'),
    #     (4, 'Very Good'),
    #     (5, 'Excellent')
    # )


class Comment(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    commented_on = models.DateTimeField(auto_now_add=True)
