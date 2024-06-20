from django.db import models

class AboutPageDetails(models.Model):
    details_heading = models.TextField()
    details_content = models.TextField()
    
class AboutPageSubHeadingsDetails(models.Model):
    details_subHeadingIcon = models.FileField(upload_to="aboutpage/",max_length=250,null=True,default=None)
    details_subHeading = models.CharField(max_length=200)
    details_subHeadingContent = models.TextField()
    
class AboutPageTrustedBy(models.Model):
    trustedByIcon = models.FileField(upload_to="aboutpage/",max_length=250,null=True,default=None)
# Create your models here.
