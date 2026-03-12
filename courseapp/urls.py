from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('detail/' , views.detail, name='detail'),
    path('auth/login', views.handlelogin, name='handlelogin'),
    path('auth/signup', views.handlesignup, name='handlesignup'),
    path('payment-success/<int:course_id>/', views.payment_success, name='payment_success'),
    path('payment-cancel/', views.payment_cancel, name='payment_cancel'),
    path('payment-failed/', views.payment_failed, name='payment_failed'),
    path('checkout/<int:course_id>/', views.CreateCheckoutSessionView, name='checkout'),
]