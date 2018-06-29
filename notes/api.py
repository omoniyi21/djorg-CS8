from rest_framework import serializers, viewsets
from .models import Note
# from .models import Bookmark

class NoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Note 
        fields = ('title', 'content')

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.object.all()
    serializers_class = NoteSerializer

class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.object.all()
    serializers_class = BookmarkSerializer
    



    




