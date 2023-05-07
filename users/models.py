from django.db import models
from django.contrib.auth.models import AbstractUser
import pyotp
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=50, unique= True)