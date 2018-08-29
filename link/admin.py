from django.contrib import admin

# Register your models here.
from .models import Link

class linkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'img')
    list_display_links = ('name', 'link', 'img')
    search_fields = ('name', )
    list_per_page = 50

admin.site.register(Link, linkAdmin)
