from django.contrib import admin

# Register your models here.

from .models import project,task
admin.site.register(project)
admin.site.register(task)
