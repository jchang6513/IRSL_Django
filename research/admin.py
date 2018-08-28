from django.contrib import admin

# Register your models here.

from .models import Research, Organization

class researchAdmin(admin.ModelAdmin):
    list_display = ('start','end','title','organization')
    list_display_links = ('start','end','title','organization')
    search_fields = ('title','organization')
    list_per_page = 50
    list_filter = ('organization',)
  
admin.site.register(Organization)
admin.site.register(Research,researchAdmin)
