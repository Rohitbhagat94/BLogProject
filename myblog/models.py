from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=50)
    descrption = models.TextField()
    upload_by = models.CharField(max_length=45)
    upload_time = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')


    def __str__(self) :
        return  self.title


class contactus(models.Model):
    Emailus = models.EmailField()
    Reason = models.TextField()

class profile(models.Model):
   first_name = models.CharField(max_length=255)
   last_name = models.CharField(max_length=245)
   user = models.CharField(max_length=255)
   email = models.EmailField()
   profile_pic = CloudinaryField('profile_pic')
   about_me = models.TextField()
   

