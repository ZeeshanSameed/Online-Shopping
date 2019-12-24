from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from .models import User
from .forms import CustomerSignupForm, StoreAdminSignUpForm, Add_Address
from django.views import generic

# Create your views here.

class HomeView(generic.ListView):
    template_name = 'abay/home.html'


def Signup(request):
    return render(request, 'abay/signup.html', name = 'signup')


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignupForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home.html')


class StoreAdminSignUpView(CreateView):
    model = User
    form_class = StoreAdminSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'storeadmin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('storeadmin.html')

def Add_Address(request):
    if request.method == 'POST':
        form = Add_Address(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return 
