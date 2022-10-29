from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return f("{self.first_name} {self.last_name}")

class Song(models.Model):
    sang_by = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_released = models.DateField()
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Lyric(models.Model):
    song_for = models.ForeignKey(Song, on_delete=models.CASCADE)
    song_id = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"Lyric of {self.song_for}"
