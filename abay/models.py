from django.db import models
#from django.contrib.auth.models import User
#from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
#from django_countries.fields import CountryField


class User(AbstractUser):
    is_store_admin = models.BooleanField('store status', default=False)
    is_customer = models.BooleanField('customer status', default=False)


class StoreAdmin(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.IntegerField()
    #avatar = models.ImageField()
    location = models.CharField(max_length=50, blank=True)


'''@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Store_admin.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.Store_admin.save()
'''


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    #avatar = models.ImageField()
    location = models.CharField(max_length=50, blank=True)


class Address(models.Model):
    country = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    shipping_address = models.CharField(max_length=40)
    billing_address = models.CharField(max_length=40)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    storeadmin = models.ForeignKey(
        StoreAdmin, null=True, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    saleprice = models.IntegerField()
    storeadmin = models.ForeignKey(
        StoreAdmin, null=True, on_delete=models.CASCADE)


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total = models.IntegerField()


class Reviews(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    body = models.CharField(max_length=100)
    Rating_CHOICES = (
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
    )
    rating = models.IntegerField(choices=Rating_CHOICES, default=1)


class Comment(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    body = models.CharField(max_length=100)
