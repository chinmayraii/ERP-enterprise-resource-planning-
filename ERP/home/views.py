from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.db.models import Q

def course(request):
    return render (request,('course.html'))

def showallstudent(request):
    data=Student.objects.all()
    return render (request,'student.html',{'data':data}) 

def showallcourse(request):
    stu=Course.objects.all()
    return render (request,'course.html',{'stu':stu})        

def addstudent(request):
    name=request.POST['name']
    branch=request.POST['branch']
    course=request.POST['course']
    mob=request.POST['mob']
    mob=int(mob)
    email=request.POST['email']
    qualification=request.POST['qualification']
    passoutyear=request.POST['passoutyear']
    passoutyear=int(passoutyear)
    status=request.POST['status']
    address=request.POST['address']
    if Student.objects.filter(email=email).exists():
        messages.error(request,'Email already exists')
        data=Student.objects.all()
        return render (request,'student.html',{'data':data})    
    else:
        Student.objects.create(name=name,branch=branch,course=course,mob=mob,email=email,qualification=qualification,passoutyear=passoutyear,status=status,address=address)
        messages.success(request,'sucessfully added !!!!')
        data=Student.objects.all()
        return render (request,'student.html',{'data':data}) 

def deletestudent(request):
    sid=request.GET['sid']
    Student.objects.get(id=sid).delete()
    data=Student.objects.all()
    return render(request,"student.html",{'data':data}) 

def searchstudent(request):
    find=request.POST['name']
    s=Student.objects.filter(Q(name=find) | Q(email=find) | Q(course=find) | Q(branch=find) | Q(status=find) | Q(qualification=find)).all()
    return render(request,"student.html",{'data':s})


def updatestudent(request):
    s=Student()
    s.id=request.POST['id']
    s.name=request.POST['name']
    s.branch=request.POST['branch']
    s.course=request.POST['course']
    s.email=request.POST['email']
    mob=request.POST['mob']
    s.mob=int(mob)
    s.qualification=request.POST['qualification']
    passoutyear=request.POST['passoutyear']
    s.passoutyear=int(passoutyear)
    s.status=request.POST['status']
    s.address=request.POST['address']
    s.save()
    data=Student.objects.all()
    return render (request,'student.html',{'data':data})

def up_course(request,uid):
    res=Student.objects.get(id=uid)
    return render(request,'updatestudent.html',{'i':res})                    