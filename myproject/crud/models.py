from django.db import models

# Create your models here.
class Member(models.Model):
    firstname=models.CharField(max_length=100)
    lasttname=models.CharField(max_length=100)
    dob=models.DateField()