from rest_framework import serializers
from .models import Student,Company,Work,stateWork

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','name','major','studentID','userName','userPass')

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id','name','userName','userPass')

class WorkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('id','name','description','amount','salary','dataTimeStart','dataTimeFinish','comp')

class StateWorkSerializers(serializers.ModelSerializer):
    class Meta:
        model = stateWork
        fields = ('id','status','studentWork','Working')