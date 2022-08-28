import http
import unittest
import uuid

from tests.common import client


class TestBuilding(unittest.TestCase):
    def test_create_building(self):
        create_user_body = {
            'name': 'Dummy Name',
            'document': str(uuid.uuid4()),
            'address': 'Dummy Address',
            'email': 'a@a.com',
            'cellphone': '0800',
        }
        response = client.post(
            '/users',
            json=create_user_body,
        )

        self.assertEqual(response.status_code, http.HTTPStatus.CREATED)
        data = response.json()
        user_id = data['id']

        create_building_body = {
            'name': 'Dummy Building',
            'address': 'Dummy Address',
            'description': 'Dummy Description',
        }

        response = client.post(f'/users/{user_id}/buildings', json=create_building_body)

        self.assertEqual(response.status_code, http.HTTPStatus.CREATED)
        self.assertIsNotNone(response.text)
        data = response.json()
        self.assertEqual(data['name'], 'Dummy Building')
        self.assertIn('id', data)
        self.assertEqual(data['owner_id'], user_id)
        self.assertEqual(data['address'], 'Dummy Address')
        self.assertEqual(data['description'], 'Dummy Description')
