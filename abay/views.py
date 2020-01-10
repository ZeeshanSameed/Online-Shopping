from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView
from .models import User, Product, Order, Cart, ProductInCart
from .forms import CustomerSignupForm, StoreAdminSignUpForm, Add_Product #Add_Order  # Add_Address
from django.views import generic
from django.contrib.auth.decorators import login_required
# # Create your views here.


class HomeView(generic.ListView):
    template_name = 'abay/home.html'
    context_object_name = 'items'
    queryset = Product.objects.all()


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'abay/detail.html'


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
        # phone_number = form.cleaned_data.get('phone_numbers')
        user = form.save()
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        phone_number = form.cleaned_data.get('phone_number')
        password = form.cleaned_data.get('password1')
        # user.refresh_from_db()
        # phone = form.cleaned_data.get('phone_number')
        # user.profile.phone_number = phone
        # user.save()
        user = authenticate(username=username, password=password)
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
        # phone_number = form.cleaned_data.get('phone_numbers')
        user = form.save()
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        phone_number = form.cleaned_data.get('phone_number')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('storeadmin')

# def Add_Address(request):
#     if request.method == 'POST':
#         form = Add_Address(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.save()
#             return
@login_required
def AddProduct(request):
    if request.method == 'POST':
        form = Add_Product(request.POST)
        form.storeadmin = request.user
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('storeadmin')
    else:
        form = Add_Product(initial={
            'storeadmin': request.user
        })
    return render(request, 'abay/add-product.html', {'form': form})


def deleteProduct(request, pk, template_name='abay/confirm_delete.html'):
    obj = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('storeadmin')
    return render(request, template_name, {'object': obj})


def edit(request, pk, template_name='abay/editproduct.html'):
    item = get_object_or_404(Product, pk=pk)
    form = Add_Product(request.POST or None, instance=item)
    form.storeadmin = request.user
    if form.is_valid():
        form.save()
        return redirect('storeadmin')
    else:
        form = Add_Product(initial={
            'storeadmin': request.user.username
        })
    return render(request, template_name, {'form': form})


@login_required
def AddToCartView(request, pk, template_name='abay/cart-detail.html'):
    product = get_object_or_404(Product, pk=pk)
    cart, is_created = Cart.objects.get_or_create(customer=request.user.customer)
    product_in_cart, is_created = ProductInCart.objects.get_or_create(cart=cart, product=product)
    # import pdb; pdb.set_trace()
    # order = Order.objects.get_or_create(product=product, cart=cart)
    product_in_cart.quantity += 1
    product_in_cart.save()
    cart.save()
    return redirect('home')
    
class cart_view(generic.DetailView):
    model = Cart
    template_name = 'abay/cart.html'



    # def Order(request, template_name= 'abay/order.html')
    # if request.method == 'POST':
    #     form = Add_Order(request.POST)
    #     form.Customer = request.user
    #     if form.is_valid():
    #         order = form.save(commit=False)
    #         order.save()
    #         return redirect('home')
    # else:
    #     form = Add_Order(initial={
    #         'customer': request.user
    #     })
    # return render(request, 'abay/cart-detail.html', {'form': form})
