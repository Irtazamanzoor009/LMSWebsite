"""
URL configuration for LMSWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from LMSWebsite import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "LMS Admin"
admin.site.site_title = "Admin"
admin.site.index_title = "LMS Admin Page"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage, name="home"),
    path('about/',views.AboutPage, name="about"),
    path('blog/',views.BlogPage, name="blog"),
    path('course/',views.CoursePage, name="course"),
    path('contactus/',views.ContactUsPage, name="contactus"),
    path('blog-content/<slug>',views.BlogContent, name="blog-content"),
    path('course-inner/<slug>',views.CourseContent),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
