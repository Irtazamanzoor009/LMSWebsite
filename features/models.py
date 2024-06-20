from django.db import models

class Features(models.Model):
    featuresIcon = models.CharField(max_length=50)
    featursHeading = models.CharField(max_length=50)
    featuresDescription = models.TextField()

# Create your models here.
