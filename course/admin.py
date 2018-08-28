from django.contrib import admin

# Register your models here.

from .models import ClassName, Course

class classAdmin(admin.ModelAdmin):
	list_display = ('name','date')
	list_display_links = ('name','date')
	serach_fields = ('name',)
	list_per_page = 50

class courseAdmin(admin.ModelAdmin):
	list_display = ('class_name','date','title','handout_type')
	list_display_links = ('class_name','date','title')
	list_filter = ('class_name',)
	list_per_page = 50
	serach_fields = ('title',)

admin.site.register(ClassName,classAdmin)	
admin.site.register(Course,courseAdmin)	
