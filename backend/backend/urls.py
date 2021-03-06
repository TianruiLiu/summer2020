"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from petAdoption import views
from accounts.views import AuthViewSet, UserViewSet, SellerViewSet

router = routers.DefaultRouter()
# router.register(r'seller', views.SellerViewSet)
router.register(r'pets', views.PetViewSet)
router.register(r'users', UserViewSet)
router.register(r'seller_profile', SellerViewSet)
router.register('api/auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url('api/auth/', include('rest_auth.urls')),
    #url('api/auth/registration/', include('rest_auth.registration.urls')),
    #url(r'^account/', include('allauth.urls')),
    # url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]

