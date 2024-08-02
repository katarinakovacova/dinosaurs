from django.contrib import admin
from dinosaurs.models import Dinosaur
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  
        (                     
            'Custom Field Heading',  
            {
                'fields': (
                    'favorite_dinosaurs',
                ),
            },
        ),
    )

admin.site.register(Dinosaur)
admin.site.register(User, CustomUserAdmin)
