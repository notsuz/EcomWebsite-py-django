from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone=models.CharField(max_length=20, null=True)
    street_address=models.CharField(max_length=200)
    

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to="images")
    bio = models.TextField()
    dob = models.DateField(null=True)
    created_at = models.DateField(auto_now=True)
    

