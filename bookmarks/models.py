from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


class Bookmark(models.Model):
    
    url = models.URLField(unique = True)
    # description = models.CharField(_('description'), max_length=100)
    # note = models.TextField(_('note'),blank=True)
    title = models.CharField(('title'), max_length = 100)
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)

class PersonalBookmark(Bookmark):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    

    
    

# Create your models here.
