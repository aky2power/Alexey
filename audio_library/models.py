from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=127)
    year = models.IntegerField()

class Song(models.Model):
    name = models.CharField(max_length=127)
    genre = models.CharField(max_length=64, blank=True, null=True)
