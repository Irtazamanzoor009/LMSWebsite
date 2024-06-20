from django.contrib import admin
from contactus.models import ContactUsAdress,ContactUsEmail,ContactUsPhone

class ContactUsAdressAdmin(admin.ModelAdmin):
    list_display = ['contactUsAddress']
    
class ContactUsPhoneAdmin(admin.ModelAdmin):
    list_display = ['contactUsPhone']
    
class ContactUsEmailAdmin(admin.ModelAdmin):
    list_display = ['contactUsEmail']
    
admin.site.register(ContactUsAdress,ContactUsAdressAdmin)
admin.site.register(ContactUsPhone,ContactUsPhoneAdmin)
admin.site.register(ContactUsEmail,ContactUsEmailAdmin)

# Register your models here.
