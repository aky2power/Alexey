from django.shortcuts import render, render_to_response

from rest_framework.viewsets import ModelViewSet

from audio_library.models import Song
from audio_libary.serializers import SongSerializer
# Create your views here.
def get_songs(request):
    songs = Song.objects.all()
    return render_to_response('index.html', context={'songs': songs})


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer