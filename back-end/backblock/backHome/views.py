from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import Student,Company,Work,stateWork
from .serializers import StudentSerializers,CompanySerializers,WorkSerializers,StateWorkSerializers



class WorktoList(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializers

class WorktoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializers

class StudenttoList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudenttoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class CompanytoList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

class CompanytoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers  

class statusWorktoList(generics.ListCreateAPIView):
    queryset = stateWork.objects.all()
    serializer_class = StateWorkSerializers

class statusWorktoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = stateWork.objects.all()
    serializer_class = StateWorkSerializers     


# Create your views here.
