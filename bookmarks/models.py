from django.db import models

class Bookmark(models.Model):
    url = models.URLField(unique = True)
    title = models.CharField(_('title'), max_length = 100)
    
    

# Create your models here.
