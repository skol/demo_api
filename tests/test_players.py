# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase


class PlayerTests(APITestCase):
    def test_player_creation(self):
        data = {
            "name": "Test players fine"
        }
        response = self.client.post('/api/players/', data, format='json')
        self.assertEqual(response.status_code, 201)
        response = self.client.get('/api/players/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test players fine')
        response = self.client.post('/api/players/', data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_player_update(self):
        data = {
            "name": "Test players fine"
        }
        response = self.client.post('/api/players/', data, format='json')
        self.assertEqual(response.status_code, 201)
        
        response = self.client.get('/api/players/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        pk = response.data[0]['id']
        
        data = {
            "name": "Second test fine"
        }
        response = self.client.put('/api/players/{}/'.format(pk), data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Second test fine')
        
        response = self.client.get('/api/players/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Second test fine')
