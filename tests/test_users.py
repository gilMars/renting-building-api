import http
import unittest
import uuid

from tests.common import client


class TestUser(unittest.TestCase):
    def test_create_user(self):
        body = {
            'name': 'Dummy Name',
            'document': str(uuid.uuid4()),
            'address': 'Dummy Address',
            'email': 'a@a.com',
            'cellphone': '0800',
        }
        response = client.post(
            '/users',
            json=body,
        )

        self.assertEqual(response.status_code, http.HTTPStatus.CREATED)
        self.assertIsNotNone(response.text)
        data = response.json()
        self.assertEqual(data['email'], 'a@a.com')
        self.assertIn('id', data)
        user_id = data['id']

        response = client.get(f'/users/{user_id}')
        assert response.status_code == 200, response.text
        data = response.json()
        self.assertEqual(data['email'], 'a@a.com')
        self.assertEqual(data['id'], user_id)
