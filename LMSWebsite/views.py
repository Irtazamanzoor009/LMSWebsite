from django.shortcuts import render
from features.models import Features
from courses.models import Courses, CourseLastDate, CourseLearn, CourseInclude
from experts.models import Experts
from django.core.exceptions import ObjectDoesNotExist
from aboutpage.models import AboutPageTrustedBy,AboutPageDetails, AboutPageSubHeadingsDetails
from blogs.models import Blogs
from contactus.models import ContactUsPhone,ContactUsAdress,ContactUsEmail

def HomePage(request):
    featuresData = Features.objects.all().order_by('id')[:3]
    courseData = Courses.objects.all().order_by('id')[:6]
    expertsData = Experts.objects.all().order_by('id')[:4]
    try:
        CountDownTime = CourseLastDate.objects.first()
        countdown_date = CountDownTime.courseLastDate if CountDownTime else None
    except ObjectDoesNotExist:
        countdown_date = None
    data = {
        'courseData':courseData,
        'featuresData':featuresData,
        'CountDownTime': countdown_date,
        'expertsData' : expertsData,
        'page_title':'Home Page'
    }
    return render(request,"index.html", data)



def AboutPage(request):
    featuresData = Features.objects.all().order_by('id')[:3]    
    try:
        aboutPagedetails = AboutPageDetails.objects.first()
    except ObjectDoesNotExist:
        aboutPagedetails = None
    
    aboutpageSubheadingDetails = AboutPageSubHeadingsDetails.objects.all().order_by('id')
    trustedByIcons = AboutPageTrustedBy.objects.all().order_by('id')
    data = {
        'featuresData':featuresData,
        'aboutPageHeadings':aboutPagedetails,
        'aboutpagesubheadingdetails':aboutpageSubheadingDetails,
        'trustedByIcons':trustedByIcons,
        'page_title':'About Page'
    }
    return render(request,"about.html", data)

def BlogPage(request):
    blogcontent = Blogs.objects.all().order_by('id')
    data = {
        'blogcontent':blogcontent,
        'page_title':'Blog Page'
    }
    return render(request, "blog.html", data)

def BlogContent(request,slug):
    blogdetails = Blogs.objects.get(blog_slug = slug)
    data = {
        'blogdetails':blogdetails
    }
    return render(request,"post.html",data)

def CoursePage(request):
    courseData = Courses.objects.all().order_by('id')
    data = {
        'courseData':courseData,
        'page_title':'Course Page'
    }
    return render(request,"course.html", data)

def CourseContent(request,slug):
    coursedetails = Courses.objects.get(course_slug = slug)
    courseLearn = CourseLearn.objects.all()
    courseInclude = CourseInclude.objects.all()
    data = {
        'courselearn':courseLearn,
        'courseinclude':courseInclude,
        'coursedetails':coursedetails,
        'page_title':'Course-content Page'
    }
    return render(request,"course-inner.html",data)

def ContactUsPage(request):
    contactaddress = ContactUsAdress.objects.all().order_by('id')
    contactphone = ContactUsPhone.objects.all().order_by('id')
    contactemail = ContactUsEmail.objects.all().order_by('id')
    data = {
        'contactaddress':contactaddress,
        'contactphone':contactphone,
        'contactemail':contactemail,
        'page_title':'Contact Us Page'
    }
    return render(request, "contactus.html", data)