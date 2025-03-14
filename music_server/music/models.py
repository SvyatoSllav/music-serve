from django.db import models

class MusicFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='music_files/')

    def __str__(self):
        return self.title