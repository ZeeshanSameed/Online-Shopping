from django.test import TestCase
import pytest
from mixer.backend.django import mixer
from abay import models
from django.contrib.auth import get_user_model
# import unittest.mock import patch
pytestmark = pytest.mark.django_db


class TestProduct:
    def test_product_is_adding(self):
        obj = mixer.blend('abay.Product')
        assert obj.pk == 1, 'should create a product instance'


class TestProfile(TestCase):
    def setup(self):
        user = models.User.objects.create(
            email='example@abc.com', password='password')
        profile = models.ProfileModel.objects.create(
            user=user, country_code='121', phone='12345678')

    def test_get_profiles_(self):
        user = get_user_model()
        user = models.User.objects.create(
            email='example@abc.com', password='password')
        # profile = models.ProfileModel.objects.create(user = user, country_code='121', phone='12345678')
        self.assertEqual(user.email, 'example@abc.com')
        self.assertTrue(user.password)
        self.assertTrue(user.email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        # self.assertEqual(profile.country_code == '121')
        # self.assertEqual(profile.phone == '12345678')

    def test_get_or_create_profile_model(self):
        user = models.User.objects.create(username="james1", email='exampl1e@abc1.com', password='password1')
        profile = models.ProfileModel.objects.create(
            user=user, country_code='1211', phone='123456781')
        with self.assertRaises(KeyError):
            models.ProfileModel.objects.create(user=None)
            models.ProfileModel.objects.create(user_id='')

    def test_get_profile_country_code(self):
        user2 = models.User.objects.create(username="james2", email='example2@abc2.com', password='password2')
        user2.profilemodel.country_code = '1212'
        user2.save()

        # profile = models.ProfileModel.objects.create(
        #     user=user2, country_code='1212', phone='123456782')
        self.assertEqual(user2.profilemodel.country_code, '1212')

    def test_get_profile_phone(self):
        user = models.User.objects.create(username="james3", email='example3@abc3.com', password='password3')
        reload_profile = models.ProfileModel.objects.get(pk=user.profilemodel.pk)
        import pdb; pdb.set_trace()
        self.assertEqual(reload_profile.get_phone_number(), '')
        
        # Set phone number
        user.profilemodel.phone = '123456783'
        user.profilemodel.save()
        user.save()
        reload_profile = models.ProfileModel.objects.get(pk=user.profilemodel.pk)
        self.assertEqual(reload_profile.get_phone_number(), '123456783')
