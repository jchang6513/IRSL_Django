from django.contrib import admin

# Register your models here.

from .models import JYLiu_CV
from .models import Member
from .models import Past
from .models import Graduate

class memberAdmin(admin.ModelAdmin):
    list_display = ('english', 'chinese', 'identity')
    list_display_links = ('english', 'chinese')
    search_fields = ('english','chinese','identity')
    list_per_page = 50
    list_filter = ('identity',)

class pastAdmin(admin.ModelAdmin):
    list_display = ('chinese', 'start', 'end', 'identity')
    list_display_links = ('chinese',)
    search_fields = ('chinese','title')
    list_per_page = 50
    ordering = ('-end',)
    list_filter = ('identity',)

admin.site.register(JYLiu_CV)
admin.site.register(Member, memberAdmin)
admin.site.register(Past, pastAdmin)
admin.site.register(Graduate, pastAdmin)
