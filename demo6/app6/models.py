from django.db import models

# Create your models here.

class HomePage(models.Model):
    name = models.CharField(default = "",max_length=100)
    Email = models.EmailField(default = "",max_length=100)
    # dob = models.DateField(blank=True,null=True,auto_now=False)
    # join_time = models.DateTimeField(blank=True,null=True,auto_now_add=True)
    password= models.CharField(default = "", max_length=50)
    cpassword  = models.CharField(default="",max_length=100)
    phone = models.CharField(max_length=10,default="")
    
    # u_img = models.ImageField(upload_to="Images_Data/",default="",max_length=200)
    # u_files = models.FileField(upload_to="Files_Data/",default="",max_length=200)
    
    def __str__(self):
        return self.name

class Admin_reg(models.Model):
    aname = models.CharField(default = "",max_length=100)
    aEmail = models.EmailField(default = "",max_length=100)
    apassword= models.CharField(default = "", max_length=50)
    acpassword  = models.CharField(default="",max_length=100)
    aphone = models.CharField(max_length=10,default="")

  
    def __str__(self):
        return self.aname