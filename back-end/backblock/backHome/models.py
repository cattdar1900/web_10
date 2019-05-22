from django.db import models
from datetime import *

class Student(models.Model):
    name = models.CharField(max_length = 50)
    major = models.CharField(max_length = 50)
    studentID = models.CharField(max_length = 50)
    userName = models.CharField(max_length = 50)
    userPass = models.CharField(max_length = 50)

class Company(models.Model):
    name = models.CharField(max_length = 50)
    userName = models.CharField(max_length = 50)
    userPass = models.CharField(max_length = 50)

    

class Work(models.Model):
    name = models.CharField(max_length = 50)  
    description = models.TextField()  
    amount = models.IntegerField()
    salary = models.IntegerField()
    dataTimeStart = models.DateTimeField(default=datetime, null=True, blank=True)
    dataTimeFinish = models.DateTimeField(default=datetime, null=True, blank=True)
    comp = models.ForeignKey(Company,null = True,on_delete=models.SET_NULL) 

STATES = (
    ('0' , 'Working'),
    ('1' , 'WorkFinished')

)
class stateWork(models.Model):
    status = models.CharField(max_length = 50, choices = STATES)
    studentWork = models.ForeignKey(Student,null = True, on_delete=models.SET_NULL)
    Working = models.ForeignKey(Work,null = True, on_delete=models.SET_NULL)





# Create your models here.
