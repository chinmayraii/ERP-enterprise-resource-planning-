from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.course),
    path('showallcourse',views.showallcourse),
    path('addstudent',views.addstudent),
    path('showallstudent',views.showallstudent),
    path('deletestudent',views.deletestudent),
    path('searchstudent',views.searchstudent),
    path('updatestudent',views.updatestudent),
    path('up_course/<int:uid>/',views.up_course),

]