from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField

class CourseInclude(models.Model):
    courseIncludeIcon = models.CharField(max_length=250)
    courseIncludecontent = models.CharField(max_length=100)
    
class CourseLearn(models.Model):
    learnContent = models.CharField(max_length=100)

class Courses(models.Model):
    courseImage = models.FileField(upload_to="courses/",max_length=250,null=True,default=None)
    courseUpdateDate = models.DateField(auto_now=True)
    courseName = models.CharField(max_length=50)
    coursePrice = models.CharField(max_length=50)
    courseDesc = models.TextField()
    courseInstructor = models.CharField(max_length=100)
    courseInstructorJob = models.CharField(max_length=200)
    CourseOverView = HTMLField()
    course_slug = AutoSlugField(populate_from='courseName',unique=True,null=True,default=None)

    
class CourseLastDate(models.Model):
    courseLastDate = models.DateTimeField()

# Create your models here.
