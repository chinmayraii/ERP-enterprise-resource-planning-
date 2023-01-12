from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.course),
    path('showallcourse',views.showallcourse),
    path('addcourse',views.addcourse),
    path('searchcourse',views.searchcourse),
    path('deletecourse',views.deletecourse),
    path('updatecourse',views.updatecourse),
    path('up_course/<int:uid>/',views.up_course),
    path('student',views.student),
    path('addstudent',views.addstudent),
    path('showallstudent',views.showallstudent),
    path('deletestudent',views.deletestudent),
    path('searchstudent',views.searchstudent),
    path('updatestudent',views.updatestudent),
    path('up_student/<int:uid>/',views.up_student),

]