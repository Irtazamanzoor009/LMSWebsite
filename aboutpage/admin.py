from django.contrib import admin
from aboutpage.models import AboutPageDetails, AboutPageTrustedBy, AboutPageSubHeadingsDetails

class AboutPageDetailsAdmin(admin.ModelAdmin):
    list_display = ('details_heading','details_content')
    
class AboutPageDetailsSubHeadingAdmin(admin.ModelAdmin):
    list_display = ('details_subHeadingIcon','details_subHeading','details_subHeadingContent')
    
class AboutPageTrusedByAdmin(admin.ModelAdmin):
    list_display = ['trustedByIcon']

admin.site.register(AboutPageDetails,AboutPageDetailsAdmin)
admin.site.register(AboutPageTrustedBy,AboutPageTrusedByAdmin)
admin.site.register(AboutPageSubHeadingsDetails,AboutPageDetailsSubHeadingAdmin)
# Register your models here.
