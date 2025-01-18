"""
URL configuration for christian_nouboukpo_et_salim_bittar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from front import views as front_views
from myauth import views as myauth_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('manage/', admin.site.urls),
    path('', front_views.home, name='home'),
    path('about/', front_views.about, name='about'),
    path('contact/', front_views.contact, name='contact'),
    path('cars/', front_views.cars, name='cars'),
    path('services/', front_views.services, name='services'),
    path('blog/', front_views.blog, name='blog'),
    path('details/<int:id>/', front_views.vehicle_details, name='vehicle_details'),
    path('login', 
         view=LoginView.as_view(template_name='myauth/login.html', next_page='home', redirect_authenticated_user=True),
         name='login'),
    path('logout', 
         view=LogoutView.as_view(next_page='home'),
         name='logout'),
    path('register', myauth_views.register, name='register'),
    path('forgot_password', myauth_views.forgot_password, name='forgot_password'),
    path('updatepassword/<str:token>/<str:uid>', myauth_views.update_password, name='update_password'),
    path('cart/', front_views.cart, name='cart'),
    path('checkout', front_views.checkout, name='checkout'),
    path('get_vehicle_details/', front_views.get_vehicle_details, name='vehicle_details'),
    path('validation/', front_views.validation, name='validation'),
    path('my_locations/', front_views.my_locations, name='my_locations'),
    path('submit_review/<int:location_id>/', front_views.submit_review, name='submit_review'),
]