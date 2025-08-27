# -*- coding: utf-8 -*-
from datetime import datetime

from django.core.validators import MaxValueValidator
from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Album(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField(validators=[MaxValueValidator(datetime.now().year)])
    players = models.ManyToManyField(Player, through='AlbumPlayers', related_name='albums')
    songs = models.ManyToManyField('Song', through='AlbumSongs', related_name='albums')
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'year'], name='unique_album'),
        ]

class AlbumPlayers(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['album', 'player'], name='unique_album_player')
        ]

class Song(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_song'),
        ]

class AlbumSongs(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='asongs')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='salbums')
    in_album_order = models.IntegerField(validators=[MaxValueValidator(99)])
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['album', 'song'], name='unique_album_song'),
            models.UniqueConstraint(fields=['album', 'in_album_order'], name='unique_album_order')
        ]