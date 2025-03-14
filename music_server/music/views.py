from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import MusicFile
import random

def serve_random_music(request):
    # Get a random music file
    music_files = MusicFile.objects.all()
    if not music_files:
        return HttpResponse("No music files available.", status=404)

    random_music = random.choice(music_files)
    return FileResponse(random_music.file)