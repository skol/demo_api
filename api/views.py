# -*- coding: utf-8 -*-
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Album, Player, Song
from .serializers import AlbumSerializer, PlayerSerializer, SongSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    # queryset = Album.objects.all()
    queryset = Album.objects.prefetch_related(
        'asongs__song'
    )
    serializer_class = AlbumSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    
    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        return Response(
            {
                'detail': 'Method "PATCH" not allowed.',
                'available_methods': ['GET', 'POST', 'PUT', 'DELETE']
            },
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        return Response(
            {
                'detail': 'Method "PATCH" not allowed.',
                'available_methods': ['GET', 'POST', 'PUT', 'DELETE']
            },
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
