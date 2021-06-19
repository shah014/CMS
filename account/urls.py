from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('', views.home, name='home'),
    path('user/', views.userPage, name='user'),

    path('product/', views.product, name="product"),
    # path('customer/', views.customer),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]





