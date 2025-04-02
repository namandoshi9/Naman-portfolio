# portfolio/admin.py
from django.contrib import admin
from .models import Resume, Project

admin.site.register(Resume)

# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ("title", "category")


from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3  # Allow uploading 3 extra images by default

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

admin.site.register(Project, ProjectAdmin)
