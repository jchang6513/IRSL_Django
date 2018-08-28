from django.db import models

# Create your models here.

class News(models.Model):
	date = models.DateField();
	content = models.TextField(blank=True);
	more = models.URLField(blank=True);

	class Meta:
		verbose_name_plural = 'News'
		ordering = ['-date']

	def __str__(self):
		return self.content
