from django.contrib import admin
from .models import Profile

#admin.site.unregister(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  list_display = [field.name for field in Profile._meta.get_fields()]
