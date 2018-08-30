from django.db import models

# Create your models here.
class Link(models.Model):
    english = models.CharField(max_length=30);
    chinese = models.CharField(max_length=30);
    link = models.URLField();
    img  = models.FileField(null=True, blank=True, upload_to='link_thumbnail/', default='link_thumbnail/website.png', help_text='recommended upload square image');

    def __str__(self):
        return self.english
