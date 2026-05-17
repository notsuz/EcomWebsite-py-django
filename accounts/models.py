from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone=models.CharField(max_length=20, null=True)
    street_address=models.CharField(max_length=200)
    

# Create your models here.
