from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(MLSAProgram)
class MLSAProgramAdmin(admin.ModelAdmin):
    list_display = ("event_title", "event_comments", )
    list_filter = ("created", )
    search_fields = ("event_title__icontains", )
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass