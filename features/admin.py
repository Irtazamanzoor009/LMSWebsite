from django.contrib import admin
from features.models import Features

class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('featuresIcon','featursHeading','featuresDescription')
    
admin.site.register(Features,FeaturesAdmin)

# Register your models here.
