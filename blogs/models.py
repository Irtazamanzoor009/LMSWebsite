from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class Blogs(models.Model):
    blog_image = models.FileField(upload_to="blogs/",max_length=250,null=True,default=None)
    blog_heading = models.CharField(max_length=200)
    blog_paragraph = HTMLField()
    blog_slug = AutoSlugField(populate_from='blog_heading',unique=True,null=True,default=None)

# Create your models here.
