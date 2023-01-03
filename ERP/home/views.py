from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.db.models import Q

def index(request):
    data=Students.objects.all()
    return render (request,'index.html',{'data':data})

def showall(request):
    data=Students.objects.all()
    return render (request,'index.html',{'data':data})    

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
    if Students.objects.filter(email=email).exists():
        messages.error(request,'Email already exists')
        data=Students.objects.all()
        return render (request,'index.html',{'data':data})    
    else:
        Students.objects.create(name=name,branch=branch,course=course,mob=mob,email=email,qualification=qualification,passoutyear=passoutyear,status=status,address=address)
        messages.success(request,'sucessfully added !!!!')
        data=Students.objects.all()
        return render (request,'index.html',{'data':data}) 

def deletestudent(request):
    sid=request.GET['sid']
    Students.objects.get(id=sid).delete()
    data=Students.objects.all()
    return render(request,"index.html",{'data':data}) 

def searchstudent(request):
    find=request.POST['name']
    s=Students.objects.filter(Q(name=find) | Q(email=find) | Q(course=find) | Q(branch=find) | Q(status=find)).all()
    return render(request,"index.html",{'data':s})            