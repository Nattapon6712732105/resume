from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('forpage/', views.forpage, name='forpage'),
    path('multiply/', views.multiply, name='multiply_page'),
    path('students/', views.students, name='students_page'),
]