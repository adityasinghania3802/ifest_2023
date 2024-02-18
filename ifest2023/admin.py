from django.contrib import admin
from .models import *

# Register your models here.

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'university','gold')
#     search_fields = ('university', 'contact_number', )

# admin.site.register(Profile, ProfileAdmin)


admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(Registration)
admin.site.register(campusAmbassador)
