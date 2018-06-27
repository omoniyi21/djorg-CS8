from django.db import models
from uuid import uuid4

class Bookmark(models.Model):
    
    url = models.URLField(unique = True)
    # description = models.CharField(_('description'), max_length=100)
    # note = models.TextField(_('note'),blank=True)
    # title = models.CharField(_('title'), max_length = 100)
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)

    
    

# Create your models here.
