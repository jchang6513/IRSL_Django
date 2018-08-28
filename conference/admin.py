from django.contrib import admin

# Register your models here.

from .models import Conference
from .models import Oral

class confAdmin(admin.ModelAdmin):
    list_display = ('start','end','title','location')
    list_display_links = ('start','end','title','location')
    search_fields = ('title','location')
    list_per_page = 50


class oralAdmin(admin.ModelAdmin):
    list_display = ('date','title','location')
    list_display_links = ('date','title','location')
    search_fields = ('title','location')
    list_per_page = 50

admin.site.register(Conference,confAdmin)
admin.site.register(Oral,oralAdmin)

