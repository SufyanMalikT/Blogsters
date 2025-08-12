from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Blog)
admin.site.register(models.Category)
admin.site.register(models.Profile)
admin.site.register(models.ProfilePic)
admin.site.register(models.Messages)