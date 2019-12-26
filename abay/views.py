from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.views.generic import CreateView
from .models import User, Product
from .forms import CustomerSignupForm, StoreAdminSignUpForm  # Add_Address
from django.views import generic

# # Create your views here.


class HomeView(generic.ListView):
    template_name = 'abay/home.html'
    context_object_name = 'items'
    queryset = Product.objects.all()


class StoreView(generic.ListView):
    template_name = 'abay/storeadmin.html'
    context_object_name = 'items'
    queryset = Product.objects.all()


def Signup(request):
    return render(request, 'abay/signup.html')


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignupForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        phone_number = form.cleaned_data.get('phone_numbers')
        user = form.save()

        # user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect('home')


class StoreAdminSignUpView(CreateView):
    model = User
    form_class = StoreAdminSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'storeadmin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        phone_number = form.cleaned_data.get('phone_numbers')
        user = form.save()
        login(self.request, user)
        return redirect('storeadmin')

# def Add_Address(request):
#     if request.method == 'POST':
#         form = Add_Address(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.save()
#             return
