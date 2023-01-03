from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('addstudent',views.addstudent),
    path('showall',views.showall),
    path('deletestudent',views.deletestudent),
    path('searchstudent',views.searchstudent),
]