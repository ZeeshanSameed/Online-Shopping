from django.test import TestCase

import pytest
import decorator
from abay import forms
from abay import models
pytestmark = pytest.mark.django_db


class TestAddProductForm(TestCase):
    def setup(self):
        pass

    def test_product_form_is_valid(self):
        user = models.User.objects.create(username="james", password="password", is_store_admin=True)
        store_admin = models.StoreAdmin.objects.create(user=user, phone_number="123456789")
        product = models.Product.objects.create(
            storeadmin=store_admin,
            name="broom",
            description="cleans at its best",
            price=19,
            saleprice=15,
        )

        data = {
            'storeadmin': store_admin.pk,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'saleprice': product.saleprice
        }
        form = forms.Add_Product(data=data)
        self.assertTrue(form.is_valid(), 'form is valid because every data is legal')
        self.assertFalse(form.errors, 'no error are shown because form is valid')

    def test_product_form_is_not_valid(self):
        user = models.User.objects.create(username="james", password="password", is_store_admin=True)
        store_admin = models.StoreAdmin.objects.create(user=user, phone_number="123456789")
        product = models.Product.objects.create(
            storeadmin=store_admin,
            name="broom",
            description="cleans at its best",
            price=19.99,
            saleprice=15,
        )

        data = {
            'storeadmin': store_admin.pk,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'saleprice': product.saleprice
        }
        form = forms.Add_Product(data=data)
        self.assertFalse(form.is_valid(), 'form is in valid because data is not legal')
        self.assertTrue(form.errors, 'errors are due to the illegal data format')