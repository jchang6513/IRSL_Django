from django.contrib import admin

# Register your models here.
from .models import Link

class linkAdmin(admin.ModelAdmin):
    list_display = ('english', 'chinese', 'link', 'img')
    list_display_links = ('english', 'chinese', 'link', 'img')
    search_fields = ('english', 'chinese', )
    list_per_page = 50

admin.site.register(Link, linkAdmin)
