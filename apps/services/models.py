from django.db import models

from apps.accounts.models import Customer

# Create your models here.

class UserGroup(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(Customer, related_name='user_groups')  # Assuming Customers are Users
    service = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='user_groups')  # One-to-One with Service

class Service(models.Model):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    licenseKey = models.CharField(max_length=255, null=True, blank=True)

class Device(models.Model):
    hardwareID = models.OneToOneField('HardwareID', on_delete=models.CASCADE)
    networkID = models.OneToOneField('NetworkID', on_delete=models.CASCADE)
    softwareID = models.OneToOneField(Service, on_delete=models.CASCADE)  # Assuming Software ID references Service
    assignedTo = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)  # Link to Customer if needed

class HardwareID(models.Model):
    identifier = models.CharField(max_length=255, unique=True)

class NetworkID(models.Model):
    identifier = models.CharField(max_length=255, unique=True)