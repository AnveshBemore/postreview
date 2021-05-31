from django.db import models

# Create your models here.
class udetails(models.Model):
    
    uname=models.CharField(max_length=100,default="",primary_key=True)
    email=models.EmailField(max_length=254, default="")
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.uname
class curntUser(models.Model):
    
    uname=models.CharField(max_length=100,default="",primary_key=True)
    def __str__(self):
        return self.uname


class postdb(models.Model):
    uname=models.CharField(max_length=100,default="")
    post_img=models.ImageField(upload_to="media")
    post_caption=models.CharField(max_length=300,default="")
    post_reviews=models.CharField(max_length=300,default="")
    def __str__(self):
        return str(self.post_img)