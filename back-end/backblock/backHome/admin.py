from django.contrib import admin
from .models import Student,Company,Work,stateWork

admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Work)
admin.site.register(stateWork)

# Register your models here.
