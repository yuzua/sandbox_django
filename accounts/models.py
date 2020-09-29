<<<<<<< HEAD
from django.db import models

# Create your models here.
=======
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    class Meta:
        verbose_name_plural = 'CustomUser'
>>>>>>> upstream/master
