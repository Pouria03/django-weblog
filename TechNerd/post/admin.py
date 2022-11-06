from django.contrib import admin
from . import models

# modify admin panel
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    search_fields = ('title','slug')
    prepopulated_fields = {'slug': ('title',)}

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','tags','created_date','category')
    search_fields = ('title','slug','body')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('id',)
    sortable_by = ('created_date','id')



# register models
admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Post,PostAdmin)
admin.site.register(models.PostVote)
admin.site.register(models.Comment)

