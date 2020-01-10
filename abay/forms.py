from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
# from django.contrib.auth.models import User
from abay.models import User, StoreAdmin, Customer, Product, Order  # Address
# from django.core.files.images import get_image_dimensions


class CustomerSignupForm(UserCreationForm):
    # first_name = forms.CharField(
    #     max_length=30, required=False, help_text='Enter Your First Name.')
    # last_name = forms.CharField(
    #     max_length=30, required=False, help_text='Enter Your Last Name.')
    email = forms.EmailField(max_length=254, help_text='username@email.com')
    phone_number = forms.CharField(
        max_length=20, help_text='Enter Your Number')

#     def clean_avatar(self):
#         avatar = self.cleaned_data['avatar']

#         try:
#             w, h = get_image_dimensions(avatar)

#             # validate dimensions
#             max_width = max_height = 100
#             if w > max_width or h > max_height:
#                 raise forms.ValidationError(
#                     u'Please use an image that is '
#                     '%s x %s pixels or smaller.' % (max_width, max_height))

#             # validate content type
#             main, sub = avatar.content_type.split('/')
#             if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
#                 raise forms.ValidationError(u'Please use a JPEG, '
#                                             'GIF or PNG image.')

#             # validate file size
#             if len(avatar) > (20 * 1024):
#                 raise forms.ValidationError(
#                     u'Avatar file size may not exceed 20k.')

#         except AttributeError:
#             """
#             Handles case when we are updating the customer profile
#             and do not supply a new avatar
#             """
#             pass

#         return avatar
#
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username',
                  'email',
                  'password1',
                  'password2',
                  'phone_number',
                  ]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        return user


class StoreAdminSignUpForm(UserCreationForm):
    # first_name = forms.CharField(
    #     max_length=30, required=False, help_text='Enter Your First Name.')
    # last_name = forms.CharField(
        # max_length=30, required=False, help_text='Enter Your Last Name.')
    email = forms.EmailField(max_length=254, help_text='username@email.com')
    phone_number = forms.IntegerField(help_text='Enter Your Number')

    # def clean_avatar(self):
    #         avatar = self.cleaned_data['avatar']

    #         try:
    #             w, h = get_image_dimensions(avatar)

    #             # validate dimensions
    #             max_width = max_height = 100
    #             if w > max_width or h > max_height:
    #                 raise forms.ValidationError(
    #                     u'Please use an image that is '
    #                     '%s x %s pixels or smaller.' % (max_width, max_height))

    #             # validate content type
    #             main, sub = avatar.content_type.split('/')
    #             if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
    #                 raise forms.ValidationError(u'Please use a JPEG, '
    #                                             'GIF or PNG image.')

    #             # validate file size
    #             if len(avatar) > (20 * 1024):
    #                 raise forms.ValidationError(
    #                     u'Avatar file size may not exceed 20k.')

    #         except AttributeError:
    #             """
    #             Handles case when we are updating the user profile
    #             and do not supply a new avatar
    #             """
    #             pass

    #         return avatar

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username',
                  'email',
                  'password1',
                  'password2',
                  'phone_number',
                  ]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_stor_admin = True
        user.save()
        storeadmin = StoreAdmin.objects.create(user=user)
        return user

#     class Add_Address(forms.ModelForm):
#         customer = forms.ModelChoiceField(queryset=Customer.objects.all())
#         storeadmin = forms.ModelChoiceField(queryset=StoreAdmin.objects.all())

#         class Meta():
#             model = Address
#             fields = [
#                 'customer', 'shipping_address', 'billing_address', ' storeadmin'
#             ]


class Add_Product(forms.ModelForm):
    storeadmin = forms.ModelChoiceField(queryset=User.objects.all(),
                                        widget=forms.HiddenInput)

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'saleprice',
        ]


# class Add_Order(forms.ModelForm):
#     customer = forms.ModelChoiceField(queryset=User.objects.all(),
#                                       widget=forms.TextInput(
#         attrs={'class': 'special'}))
#     products = forms.ModelMultipleChoiceField(queryset=Product.objects.all())

#     class Meta:
#         model = Order
#         fields = [
#             # 'product',
#             'total',
#         ]
#         exclude = [
#             'ordered_at'
#         ]
