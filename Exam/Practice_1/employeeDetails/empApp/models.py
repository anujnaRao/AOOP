from django.db import models


# Create your models here.
class Employee(models.Model):
    usn = models.IntegerField()
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
