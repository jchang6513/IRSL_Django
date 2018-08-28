from django.contrib import admin

# Register your models here.

from .models import Publication_List, International, Domestic, Book

class pubAdmin(admin.ModelAdmin):
    list_display = ('NO', 'author', 'title')
    list_display_links = ('NO', 'author', 'title')
    search_fields = ('author', 'title')
    list_per_page = 50

admin.site.register(Publication_List)
admin.site.register(International, pubAdmin)
admin.site.register(Domestic, pubAdmin)
admin.site.register(Book, pubAdmin)
