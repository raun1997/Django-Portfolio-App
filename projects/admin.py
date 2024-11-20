from django.contrib import admin
from projects.models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass

# registering the model created by us
admin.site.register(Project, ProjectAdmin)
