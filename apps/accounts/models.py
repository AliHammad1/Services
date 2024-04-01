from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.JSONField()
    phoneNumbers = models.JSONField()
    registrationDate = models.DateField(default=timezone.now)

class Partner(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    # services = models.ManyToManyField('Service', related_name='partners')
    contact = models.JSONField()
