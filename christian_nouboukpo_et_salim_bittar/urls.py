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
urlpatterns = [
    path('manage/', admin.site.urls),
    path('', front_views.home, name='home'),
    path('about/', front_views.about, name='about'),
    path('contact/', front_views.contact, name='contact'),
    path('services/', front_views.services, name='services'),
    path('blog/', front_views.blog, name='blog'),
    path('cars/', front_views.cars, name='cars'),
    # path('blog-single/', front_views.blog_single, name='blog-single'),
]
