from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_staff', 'is_active', 'notifications_enabled')
    search_fields = ('email',)
    list_filter = ('is_active', 'is_staff')

# Если вы не используете декоратор @admin.register, вы можете сделать так:
# admin.site.register(CustomUser, CustomUserAdmin)
