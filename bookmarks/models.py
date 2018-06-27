from django.db import models

class Bookmark(models.Model):
    
    url = models.URLField(unique = True)
    title = models.CharField(_('title'), max_length = 100)
    # id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    
    

# Create your models here.
