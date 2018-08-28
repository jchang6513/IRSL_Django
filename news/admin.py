from django.contrib import admin

# Register your models here.

from .models import News

class newsAdmin(admin.ModelAdmin):
    list_display = ('date', 'content')
    list_display_links = ('date', 'content')
    search_fields = ('content', )
    list_per_page = 50

admin.site.register(News, newsAdmin)
