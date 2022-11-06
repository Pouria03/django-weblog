from django.contrib import admin
from .models import About
# Register your models here.
admin.site.register(About)

admin.site.site_header = ' TechNerds AdminPanel'
admin.site.site_title = ' TechNerds '
admin.site.index_title = 'wellcome !'
