from django.db import models

# Create your models here.
class Regi(models.Model):

    username = models.CharField(max_length=10)
    emmail = models.EmailField()
    password = models.CharField(max_length=100)