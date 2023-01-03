from django.db import models



status_choice=(
    ('Enquiry','Enquiry'),
    ('Joined','Joined'),
    ('Placed','Placed'),
    ('complete','Complete'),
)

class Students(models.Model):
    name=models.CharField(max_length=30)
    branch=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    mob=models.IntegerField()
    email=models.CharField(max_length=30)
    qualification=models.CharField(max_length=30)
    passoutyear=models.IntegerField()
    status=models.CharField(choices=status_choice,max_length=30)
    address=models.TextField()
    def __str__(self) -> str:
        return self.name
    
