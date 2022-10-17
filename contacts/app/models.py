from enum import auto
from django.db import models

# Create your models here.

class Contacts(models.Model):
    ContactId = models.AutoField(primary_key=True)
    ContactName = models.CharField(max_length=100)
    ContactNumber = models.CharField(max_length=20)