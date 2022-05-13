from django.db import models

# Create your models here.
class Otp(models.Model):
    email=models.CharField(max_length=100,unique=True)
    otp=models.CharField(max_length=9,blank=True,null=True)
    count=models.IntegerField(default=0,help_text="Email of otp Send")
    validated=models.BooleanField(default=False,help_text="if true then it mean otp is validate")
    otpSessionID=models.CharField(max_length=120,null=True,default=None)
    username=models.CharField(max_length=20,blank=True,null=True,default=None)
    email=models.CharField(max_length=50,null=True,blank=True,default=True)
    password=models.CharField(max_length=100,null=True,blank=True,default=True)
