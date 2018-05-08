from rest_framework import serializers
from audio_library.models import Song

class SongSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.name')

    class Meta:
        model = Song
        fields = ('name', 'artist_name', 'genre')