# -*- coding: utf-8 -*-
from django.db import transaction
from rest_framework import serializers

from .models import Album, AlbumSongs, Player, Song


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class AlbumSongSerializer(serializers.ModelSerializer):
    song = SongSerializer()
    class Meta:
        model = AlbumSongs
        fields = ['song', 'in_album_order']
        extra_kwargs = {
            'in_album_order': {'required': True}
        }


class AlbumSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True)
    songs = AlbumSongSerializer(many=True, source='asongs')
    class Meta:
        model = Album
        fields = '__all__'

    def create(self, validated_data):
        palyers_data = validated_data.pop('players')
        songs_data = validated_data.pop('asongs')
        album, _ = Album.objects.get_or_create(**validated_data)
        for player_data in palyers_data:
            player, _ = Player.objects.get_or_create(**player_data)
            album.players.add(player)
        for song_item in songs_data:
            song_data = song_item.pop('song')
            song, _ = Song.objects.get_or_create(**song_data)
            AlbumSongs.objects.create(
                album=album,
                song=song,
                in_album_order=song_item['in_album_order']
            )
        album.refresh_from_db()
        return album
    
    @transaction.atomic
    def update(self, instance, validated_data):
        if 'players' in validated_data:
            players_data = validated_data.pop('players')
            current_players = list(instance.players.all())
            instance.players.clear()
            for player_data in players_data:
                player, _ = Player.objects.get_or_create(**player_data)
                instance.players.add(player)
            # чистим сироток
            for player in current_players:
                if player.albums.count() == 0:
                    player.delete()

        if 'asongs' in validated_data:
            songs_data = validated_data.pop('asongs')
            current_songs = list(instance.songs.all())
            instance.songs.clear()
            for song_item in songs_data:
                song_data = song_item.pop('song')
                song, _ = Song.objects.get_or_create(**song_data)
                AlbumSongs.objects.update_or_create(
                    album=instance,
                    song=song,
                    in_album_order=song_item['in_album_order']
                )
            # чистим сироток
            for song in current_songs:
                if song.albums.count() == 0:
                    song.delete()

        return super().update(instance, validated_data)
