from django.test import SimpleTestCase
from django.urls import reverse, resolve
from abay.views import Signup, CustomerSignUpView, StoreAdminSignUpView, HomeView, ProductDetailView, deleteProduct, edit, StoreView, AddProduct, AddToCartView, cart_view
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views


class TestUrls(SimpleTestCase):
    def test_signup_url_is_resolved(self):
        url = reverse('signup')
        # print (resolve(url))
        self.assertEquals(resolve(url).func, Signup)

    def test_customersignup_url_is_resolved(self):
        url = reverse('customer_signup')
        self.assertEquals(resolve(url).func.view_class, CustomerSignUpView)

    def test_storesignup_url_is_resolved(self):
        url = reverse('store_admin_signup')
        # print (resolve(url))
        self.assertEquals(resolve(url).func.view_class, StoreAdminSignUpView)

    # def test_loginview_url_is_resolved(self):
    #     url = reverse('login')
    #     # print (resolve(url))
    #     self.assertEquals(resolve(url).func.auth_views_class, LoginView)

    # def test_logoutview_url_is_resolved(self):
    #     url = reverse('logout')
    #     # print (resolve(url))
    #     self.assertEquals(resolve(url).func.auth_views_class, LogoutView)

    def test_homeview_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomeView)

    def test_productdetailview_url_is_resolved(self):
        url = reverse('detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, ProductDetailView)

    def test_deleteproductview_url_is_resolved(self):
        url = reverse('deleteProduct', args=[1])
        self.assertEquals(resolve(url).func, deleteProduct)

    def test_editview_url_is_resolved(self):
        url = reverse('edit', args=[1])
        self.assertEquals(resolve(url).func, edit)        

    def test_storeadminview_url_is_resolved(self):
        url = reverse('storeadmin')
        self.assertEquals(resolve(url).func.view_class, StoreView)

    def test_addproductview_url_is_resolved(self):
        url = reverse('addproduct')
        self.assertEquals(resolve(url).func, AddProduct)

    def test_addtocartview_url_is_resolved(self):
        url = reverse('cartdetail', args=[1])
        self.assertEquals(resolve(url).func, AddToCartView)

    def test_cartview_url_is_resolved(self):
        url = reverse('cart')
        self.assertEquals(resolve(url).func.view_class, cart_view)
