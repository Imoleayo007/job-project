from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customuser(AbstractUser):
    email = models.EmailField(blank=False, unique=True)
    first_name = models.CharField(blank=False, max_length=150)
    last_name = models.CharField(blank=False, max_length=150)

    