from django.db import models

class Experts(models.Model):
    expertImage = models.FileField(upload_to="experts/",max_length=250,null=True,default=None)
    expertName = models.CharField(max_length=50)
    expertDesc = models.CharField(max_length=50)

# Create your models here.
