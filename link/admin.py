from django.contrib import admin

# Register your models here.
from .models import Link

class linkAdmin(admin.ModelAdmin):
    list_display = ('chinese', 'english', 'link', 'img')
    list_display_links = ('chinese', 'english', 'link', 'img')
    search_fields = ('chinese', 'english')
    list_per_page = 50

admin.site.register(Link, linkAdmin)
