from django.db import models


# Create your models here.
class Employee(models.Model):
    USN = models.IntegerField()
    Name = models.CharField(max_length=20)
    Address = models.CharField(max_length=30)
