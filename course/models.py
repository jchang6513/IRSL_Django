from django.db import models

# Create your models here.

class ClassName(models.Model):
	name = models.CharField(max_length=200);
	date = models.DateField();

	class Meta:
		ordering = ['-date','name']
	
	def __str__(self):
		return self.name


class Course(models.Model):
	class_name = models.ForeignKey(ClassName,on_delete=models.CASCADE, default=1)
	date    = models.DateField(null=True, blank=True);
	title   = models.CharField(max_length=200);
	
	def content_file_name(instance, filename):
		return '/'.join(['course',instance.class_name.name,filename])

	print(content_file_name)
	handout = models.FileField(null=True, blank=True,upload_to=content_file_name);

	HANDOUT_TYPE = (
		('LC','Lecture'),
		('AP','Appendix'),
	)
	
	handout_type = models.CharField(
		max_length=2,
		choices=HANDOUT_TYPE,
		default='LC',		
	)

	class Meta:
		ordering = ['class_name','-date']


	def __str__(self):
		return self.title
