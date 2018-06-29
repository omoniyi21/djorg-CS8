from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class Note(models.Model):
    #TODO add use/author who created it 
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    title = models.CharField(max_length = 200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now=True) #difference add the time everytime its updated vvs now_add does it once intiially 
    catergory = models.CharField(max_length=100)
    # category = models.CharFields(max_length = 20)
    #TODO Tagging system or categories 
class PersonalNote(Note):
    user = models.ForeignKey(User,on_delete=models.CASCADE)







# Create your models here.
# GUID or UUID - string of characters that are higly unlikely to be duplicated 
# Bookmark app 
# -- new url more than likely 