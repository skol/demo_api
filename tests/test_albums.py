# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

from api.models import Album


class AlbumTest(APITestCase):
    def test_album_creation(self):
        data = {
            "name": "Test album",
            "year": 2023,
            "players": [
                {
                    "name": "I am"
                },
                {
                    "name": "Me"
                }
            ],
            "songs": [
                {
                    "song": {
                        "name": "Second play"
                    },
                    "in_album_order": 2
                },
                {
                    "song": {
                        "name": "First play"
                    },
                    "in_album_order": 1
                },
                {
                    "song": {
                        "name": "Last play"
                    },
                    "in_album_order": 3
                }
            ]
        }
        response = self.client.post('/api/albums/', data, format='json')
        self.assertEqual(response.status_code, 201)
        response = self.client.get('/api/players/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        response = self.client.get('/api/songs/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
    
    def test_album_update(self):
        data = {
            "name": "Test album",
            "year": 2023,
            "players": [
                {
                    "name": "I am"
                },
                {
                    "name": "Me"
                }
            ],
            "songs": [
                {
                    "song": {
                        "name": "Second play"
                    },
                    "in_album_order": 2
                },
                {
                    "song": {
                        "name": "First play"
                    },
                    "in_album_order": 1
                },
                {
                    "song": {
                        "name": "Last play"
                    },
                    "in_album_order": 3
                }
            ]
        }
        response = self.client.post('/api/albums/', data, format='json')
        self.assertEqual(response.status_code, 201)
        album = response.data
        pk = album['id']
        data = {
            "name": "Страх и ужас",
            "year": 2025,
            "players": [
                {
                    "name": "Страшила"
                }
            ],
            "songs": [
                {
                    "song": {
                        "name": "Страх"
                    },
                    "in_album_order": 1
                },
                {
                    "song": {
                        "name": "Ужас"
                    },
                    "in_album_order": 2
                }
            ]
        }
        response = self.client.put('/api/albums/{}/'.format(pk), data, format='json')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/api/albums/{}/'.format(pk), format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['players']), 1)
        response = self.client.get('/api/players/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        response = self.client.get('/api/songs/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
