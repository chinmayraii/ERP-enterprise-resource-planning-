from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.db.models import Q
import datetime

def course(request):
    cou=Course.objects.all()
    return render (request,'course.html',{'cou':cou}) 

def showallcourse(request):
    cou=Course.objects.all()
    return render (request,'course.html',{'cou':cou}) 

def addcourse(request):
    cname=request.POST['cname']
    duration=request.POST['duration']
    detail=request.POST['detail']
    fees=request.POST['fees']
    fees=int(fees)
    if Course.objects.filter(cname=cname).exists():
        messages.error(request,'Course already exists ')
        cou=Course.objects.all()
        return render(request,'course.html',{'cou':cou}) 
    else:
        Course.objects.create(cname=cname,duration=duration,details=detail,fees=fees)
        messages.success(request,'Sucessfully Added')
        cou=Course.objects.all()
        return render(request,'course.html',{'cou':cou}) 

def searchcourse(request):
    find=request.POST['name']
    c=Course.objects.filter(Q(cname=find) | Q(duration=find) | Q(details=find)).all()
    return render(request,'course.html',{'cou':c}) 

def deletecourse(request):
    cid=request.GET['cid']
    Course.objects.get(id=cid).delete()
    messages.success(request,'!!!!!! Sucessfully Deleted !!!!!')
    cou=Course.objects.all()
    return render (request,'course.html',{'cou':cou}) 

def updatecourse(request):
    c=Course()
    c.id=request.POST['id']
    c.cname=request.POST['cname']
    c.duration=request.POST['duration']
    c.details=request.POST['details'] 
    fees=request.POST['fees']
    c.fees=int(fees)
    c.save()
    messages.success(request,'!!!!! Course Updated Successfully !!!!')
    cou=Course.objects.all()
    return render (request,'course.html',{'cou':cou})

def up_course(request,uid):
    res=Course.objects.get(id=uid)
    return render(request,'updatecourse.html',{'i':res})                               

def showallstudent(request):
    stu=Student.objects.all()
    cou=Course.objects.all()
    return render (request,'student.html',{'stu':stu,'cou':cou}) 

def student(request):
    stu=Student.objects.all()
    cou=Course.objects.all()
    return render (request,'student.html',{'stu':stu,'cou':cou})     

def addstudent(request):
    s=Student()
    s.sname=request.POST['sname']
    s.branch=request.POST['branch']
    sid=request.POST['course']
    s.course=Course.objects.get(id=sid)
    mob=request.POST['mob']
    s.mob=int(mob)
    s.email=request.POST['email']
    s.qualification=request.POST['qualification']
    passoutyear=request.POST['passoutyear']
    s.passoutyear=int(passoutyear)
    s.sem=request.POST['sem']
    s.date=datetime.datetime.now()
    s.status=request.POST['status']
    s.address=request.POST['address']
    s.save()
    stu=Student.objects.all()
    cou=Course.objects.all()
    return render (request,'student.html',{'stu':stu,'cou':cou}) 

def deletestudent(request):
    sid=request.GET['sid']
    Student.objects.get(id=sid).delete()
    stu=Student.objects.all()
    return render(request,"student.html",{'stu':stu}) 

def searchstudent(request):
    find=request.POST['stuname']
    s=Student.objects.filter(Q(sname=find) | Q(email=find) | Q(course=find) | Q(branch=find) | Q(status=find) | Q(qualification=find)).all()
    return render(request,"student.html",{'stu':s})


def updatestudent(request):
    s=Student()
    s.id=request.POST['id']
    s.sname=request.POST['sname']
    s.branch=request.POST['branch']
    sid=request.POST['course']
    s.course=Course.objects.get(id=sid)
    s.email=request.POST['email']
    mob=request.POST['mob']
    s.mob=int(mob)
    s.qualification=request.POST['qualification']
    passoutyear=request.POST['passoutyear']
    s.passoutyear=int(passoutyear)
    s.status=request.POST['status']
    s.address=request.POST['address']
    s.save()
    cou=Course.objects.all()
    stu=Student.objects.all()
    return render (request,'student.html',{'stu':stu,'cou':cou})

def up_student(request,uid):
    res=Student.objects.get(id=uid)
    return render(request,'updatestudent.html',{'i':res})                    