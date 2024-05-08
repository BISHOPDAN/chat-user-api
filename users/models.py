from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    phone_number = PhoneNumberField(blank=True)
    tokens = models.IntegerField(default=4000)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    

class VerificationOtp(models.Model):
    email = models.CharField(max_length=200)
    checkotp = models.IntegerField()
       
