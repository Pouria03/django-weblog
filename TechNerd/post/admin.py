from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Post)
admin.site.register(models.PostVote)
admin.site.register(models.Comment)