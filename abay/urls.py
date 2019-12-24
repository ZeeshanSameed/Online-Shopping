from django.urls import include, path
from abay import views
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    
    path('', views.Signup, name='signup'),
    path('signup/customer', views.CustomerSignUpView.as_view(),
         name='customer_signup'),
    path('signup/store-admin', views.StoreAdminSignUpView.as_view(),
         name='store_admin_signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.HomeView.as_view(), name='home'),
]
