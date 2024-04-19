from django.db import models

# Create your models here.
class userRegister(models.Model):
    Name=models.CharField(max_length=30)
    EmailID=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)
    CPassword=models.CharField(max_length=30)
    Gender=models.CharField(max_length=30)
class contact(models.Model):
    Name=models.CharField(max_length=20)
    EmailID=models.CharField(max_length=30)
    Subject=models.CharField(max_length=30)
    Message=models.TextField()
class car(models.Model):
    Name=models.CharField(max_length=20)
    Color=models.CharField(max_length=20)
    Company=models.CharField(max_length=20)
    Rate=models.IntegerField()
    Description=models.TextField()
    Photo=models.ImageField(upload_to='static/images',default='default')
class booking(models.Model):
     Name=models.CharField(max_length=20)
     CarName=models.CharField(max_length=20,default='default')
     Date=models.DateField()
     Days=models.IntegerField()
     Proof=models.FileField(upload_to='static/proof')
     Amount=models.IntegerField()
class payments(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('success','Success'),
        ('failed','Failed'),
    ]
    Name=models.CharField(max_length=20)
    Card_Number=models.CharField(max_length=20)
    Expiration=models.CharField(max_length=20)
    CV_number=models.IntegerField()
    Amount=models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
class room(models.Model):
    Place=models.CharField(max_length=20)
    Type=models.CharField(max_length=20)
    Rate=models.IntegerField()
    Description=models.TextField()
    Photo=models.ImageField(upload_to='static/images')
class roombooking(models.Model):
     Name=models.CharField(max_length=20)
     RoomPlace=models.CharField(max_length=20,default='default')
     Date=models.DateField()
     Days=models.IntegerField()
     Proof=models.FileField(upload_to='static/proof')
     Amount=models.IntegerField()