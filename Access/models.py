from django.db import models

# Create your models here.

class Login(models.Model):
    Name = models.CharField(max_length=1000)
    Email = models.CharField(primary_key=True,max_length=500)
    Roles = models.CharField(max_length=500)
    Password = models.CharField(max_length=1000)
    Salt = models.CharField(max_length=1000)

    class Meta:
        db_table = "login"
     

class IssuList(models.Model):
    Id = models.AutoField(primary_key=True)
    Tags = models.CharField(max_length=500)    
    Body = models.CharField(max_length=20000)
    Heading = models.CharField(max_length=20000)

    class Meta:
        db_table = "issuList"

 