from django.contrib import admin
from blogs.models import Blogs

class BlogsAdmin(admin.ModelAdmin):
    list_display = ('blog_image','blog_heading','blog_paragraph')
    
admin.site.register(Blogs,BlogsAdmin)

# Register your models here.
