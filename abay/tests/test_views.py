from django.test import TestCase, Client
from django.urls import reverse, resolve
from abay.models import User, Product, Order, Cart, ProductInCart
import json


class TestViews(TestCase):
    addproduct_url = reverse('addproduct')

    def setup(self):
        self.client = Client
        # self.addproduct_url = reverse('addproduct')
        p = Product.objects.create(
            name='name',
            description='description',
            price=100,
            saleprice=80,
        )

    def test_addproduct_POST_new_product(self):
        # setup code
        client = Client
        # test code
        response = self.client.post(self.addproduct_url, {
                                    'name': 'name', 'description': 'description', 'price': 1, 'saleprice': 0})
        # assertions
        self.assertEquals(response.status_code, 302)
        # self.assertEquals(self.)

    def test_addproduct_POST_no_data(self):

        response = self.client.post(self.addproduct_url)
        # print(resolve(response))
        self.assertEqual(response.status_code, 302)

    def test_deleteproduct_is_not_working(self):
        # deleteProduct_url = reverse('deleteProduct', args=[1])
        response = self.client.get(
            reverse('deleteProduct', args=[1]), product='name', pk=1)
        r = response.status_code
        self.assertEquals(r, 404)

    def test_homeview_list_GET(self):
        response = self.client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'abay/home.html')

    
    # def test_deleteproduct_is_working(self):    

    #     p = Product.objects.create(
    #         name='name',
    #         description='description',
    #         price=100,
    #         saleprice=80,
    #     )
    #     # deleteProduct_url = reverse('deleteProduct', args=[1])
    #     response = self.client(reverse('deleteProduct','id'=1))
    #     self.assertEquals(response.status_code, 204)
