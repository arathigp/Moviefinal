from . import views
from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include

app_name='movieapp'

urlpatterns = [

    path('',views.home,name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/',views.register,name='register'),
    path('uhome/', views.uhome, name='uhome'),
    path('update/<int:id>/', views.update, name='update'),
    path('detail/<int:id>', views.detail, name='detail'),




]