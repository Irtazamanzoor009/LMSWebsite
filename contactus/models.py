from django.db import models

class ContactUsAdress(models.Model):
    contactUsAddress = models.CharField(max_length=100)

class ContactUsPhone(models.Model):
    contactUsPhone = models.CharField(max_length=100)
    
class ContactUsEmail(models.Model):
    contactUsEmail = models.CharField(max_length=100)

# Create your models here.
