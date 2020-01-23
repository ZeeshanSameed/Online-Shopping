from django.test import TestCase, Client, RequestFactory
from abay import views
from django.contrib.auth.models import AnonymousUser
from mixer.backend.django import mixer
# from django.urls import reverse, resolve
from abay.models import User, Product, Order, Cart, ProductInCart
# import jsonpaginator.py
import pytest
pytestmark = pytest.mark.django_db


class TestHomeView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        resp = views.HomeView.as_view()(req)
        assert resp.status_code == 200, 'can be called by others'


class Test_login_required_tag:
    def test_anonymous_user_cannot_access_addproduct_view(self):
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        resp = views.AddProduct(req)
        assert resp.status_code == 302, 'annonymous user is forbidden'
        # assert 'signup' in resp.url

    def test_user_can_access_addproduct_view(self):
        user = mixer.blend('abay.User', is_store_admin=True)
        req = RequestFactory().get('/')
        req.user = user
        resp = views.AddProduct(req)
        assert resp.status_code == 200, 'authenticated storeadmin can access add product view'

    def test_anonymous_user_cannot_access_addtocart(self):
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        resp = views.AddToCartView(req)
        assert resp.status_code == 302, 'annonymous user is forbidden to access this'

    def test_user_can_access_add_to_cart_view(self):
        user = mixer.blend('abay.User', is_customer=True)
        customer = mixer.blend('abay.Customer')
        product = mixer.blend('abay.Product')
        req = RequestFactory().get('/')
        req.user = customer
        resp = views.AddToCartView(req.user, product.pk)
        assert resp.status_code == 302, 'authenticated customer ccan add to cart'



# class TestViews(TestCase):
#     addproduct_url = reverse('addproduct')

#     def setup(self):
#         self.client = Client
#         # self.addproduct_url = reverse('addproduct')
#         p = Product.objects.create(
#             name='name',
#             description='description',
#             price=100,
#             saleprice=80,
#         )

#     def test_addproduct_POST_new_product(self):
#         # setup code
#         client = Client
#         # test code
#         response = self.client.post(self.addproduct_url, {
#                                     'name': 'name', 'description': 'description', 'price': 1, 'saleprice': 0})
#         # assertions
#         self.assertEquals(response.status_code, 302)
#         # self.assertEquals(self.)

#     def test_addproduct_POST_no_data(self):

#         response = self.client.post(self.addproduct_url)
#         # print(resolve(response))
#         self.assertEqual(response.status_code, 302)

#     def test_deleteproduct_is_not_working(self):
#         # deleteProduct_url = reverse('deleteProduct', args=[1])
#         response = self.client.get(
#             reverse('deleteProduct', args=[1]), product='name', pk=1)
#         r = response.status_code
#         self.assertEquals(r, 404)

#     def test_homeview_list_GET(self):
#         response = self.client.get(reverse('home'))

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'abay/home.html')


#     # def test_deleteproduct_is_working(self):

#     #     p = Product.objects.create(
#     #         name='name',
#     #         description='description',
#     #         price=100,
#     #         saleprice=80,
#     #     )
#     #     # deleteProduct_url = reverse('deleteProduct', args=[1])

#     #     response = self.client(reverse('deleteProduct','id'=1))
#     #     import pdb; pdb.set_trace()
#     #     self.assertEquals(response.status_code, 204)
