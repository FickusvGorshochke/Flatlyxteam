from django.contrib.auth.models import AbstractUser
from django.db import models

class user(AbstractUser):
    pass

# class back_log(models.Model):
#     mail = models.CharField(max_length=250)
#     try:
#         password = models.CharField(max_length=250)
#     except Exception:
#         password = models.CharField(max_length=1000)
#     number = models.IntegerField()
#
# class order(models.Model):
#     machine = models.CharField(max_length=250)
#     type = models.CharField(max_length=250)
#     date = models.DecimalField(max_digits=2, decimal_places=2)