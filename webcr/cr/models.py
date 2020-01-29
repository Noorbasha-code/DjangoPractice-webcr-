from django.db import models



# Create your models here.
class student(models.Model):
    sid =models.CharField(max_length=10)
    sname  =models.CharField(max_length=20)
    semial =models.EmailField(format(' '))
    scontacts =models.CharField(max_length=10)
    class Meta:
        db_table="student"


class Student1(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    class Meta:
        db_table="student1"
