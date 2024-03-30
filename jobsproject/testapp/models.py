from django.db import models

# Create your models here.
class Hybdjobs(models.Model):
    company=models.CharField(max_length=120)
    title=models.CharField(max_length=120)
    phonenumber=models.IntegerField()
    email=models.EmailField()
    dob=models.DateField()



class Bngjobs(models.Model):
    company = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    phonenumber = models.BigIntegerField()
    email = models.EmailField()
    dob = models.DateField()

class Punejobs(models.Model):
    company = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    phonenumber = models.BigIntegerField()
    email = models.EmailField()
    dob = models.DateField()

