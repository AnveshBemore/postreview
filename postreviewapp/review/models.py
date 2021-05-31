from django.db import models

# Create your models here.
class udetails(models.Model):
    
    uname=models.CharField(max_length=100,default="",primary_key=True)
    email=models.EmailField(max_length=254, default="")
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.uname

class crntPostUser(models.Model):    
    uname=models.CharField(max_length=100,default="",primary_key=True)
    def __str__(self):
        return self.uname

 
class crntReviewUser(models.Model):    
    uname=models.CharField(max_length=100,default="",primary_key=True)
    def __str__(self):
        return self.uname
class myreviews(models.Model):
     
    postuname=models.CharField(max_length=100,default="")
    postimg=models.ImageField(upload_to="media")
    postcaption=models.CharField(max_length=200,default="")
    review=models.CharField(max_length=300,default="")
    def __str__(self):
        return str(self.postimg)