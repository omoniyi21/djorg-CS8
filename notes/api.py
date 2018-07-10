from rest_framework import serializers, viewsets
from .models import Note
from .models import PersonalNote


class NoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Note 
        fields = ('title', 'content')
   

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote 
        fields = ('title', 'content')

    def create(self, validate_date):
        user = self.context['request'].user
        personal_note = PeronsalNote.objects.create(
            user=user, **validated_data)
        return personal_note
        

def get_queryset(self):
    user = self.request.user

    if user.is_anonymous:
        return PersonalNote.objects.none()
    else:
        return PersonalNote.objects.filter(user=user)
    



    




