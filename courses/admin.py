from django.contrib import admin
from courses.models import Courses,CourseLastDate,CourseInclude,CourseLearn


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('courseImage','courseName','coursePrice','courseDesc','courseInstructor','courseInstructorJob','CourseOverView')
    
class CourseLastDateAdmin(admin.ModelAdmin):
    list_display = ['courseLastDate']
    
class CourseIncludeAdmin(admin.ModelAdmin):
    list_display = ('courseIncludeIcon','courseIncludecontent')
    
class CourseLearnContentAdmin(admin.ModelAdmin):
    list_display = ['learnContent']
    
admin.site.register(Courses,CoursesAdmin)
admin.site.register(CourseLastDate,CourseLastDateAdmin)
admin.site.register(CourseInclude,CourseIncludeAdmin)
admin.site.register(CourseLearn,CourseLearnContentAdmin)



# Register your models here.
