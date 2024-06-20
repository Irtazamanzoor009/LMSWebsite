from django.contrib import admin
from experts.models import Experts 

class ExpertsAdmin(admin.ModelAdmin):
    list_display = ('expertImage','expertName','expertDesc')
    
admin.site.register(Experts, ExpertsAdmin)

# Register your models here.
