from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/' , views.detail, name='detail'),
    path('auth/login', views.handlelogin, name='handlelogin'),
    path('auth/signup', views.handlesignup, name='handlesignup'),
]