from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ProjectRequest)
admin.site.register(ProjectCollaborator)
admin.site.register(UserProjects)
admin.site.register(ProjectImage)