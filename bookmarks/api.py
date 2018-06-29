from rest_framework import serializers, viewsets
from .models import Bookmark

class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookmark 
        fields = ('title', 'content')

class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializers_class = BookmarkSerializer 

# class PersonalBookmarkSerializer(viewsets.ModelViewSet):
