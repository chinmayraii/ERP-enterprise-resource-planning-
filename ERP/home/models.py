from django.db import models

class Course(models.Model):
    cname=models.CharField(max_length=30)
    duration=models.CharField(max_length=30)
    details=models.CharField(max_length=100)
    fees=models.IntegerField()
    def __str__(self) -> str:
        return self.cname+" "+str(self.fees)

status_choice=(
    ('Enquiry','Enquiry'),
    ('Joined','Joined'),
    ('Placed','Placed'),
    ('complete','Complete'),
)

class Student(models.Model):
    sname=models.CharField(max_length=30)
    branch=models.CharField(max_length=30)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    mob=models.IntegerField()
    qualification=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    passoutyear=models.IntegerField()
    sem=models.CharField(max_length=30)
    date=models.DateField(auto_now=False)
    status=models.CharField(choices=status_choice,max_length=30)
    address=models.TextField()
    def __str__(self) -> str:
        return self.sname+" "+self.course.cname+" "+str(self.course.fees)

class Amount(models.Model):
    student=models.OneToOneField(Student,primary_key=True,on_delete=models.CASCADE)
    total_fee=models.IntegerField()
    submitamount=models.CharField(max_length=100)
    remaining=models.IntegerField()
    submitdate=models.CharField(max_length=100)
    nextpaydate=models.DateField(auto_now=False)
    def __str__(self) -> str:
        return self.student.sname+" "+str(self.remaining)        
    
