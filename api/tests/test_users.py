import http
import unittest
import uuid

from api.tests.common import client, create_user, mocked_user_body


class TestUser(unittest.TestCase):

    def test_create_user(self):
        response = create_user()
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

    def test_get_users_without_data(self):
        response = client.get('/users/')
        json_body = response.json()
        self.assertEqual(json_body['total'], 0)
        self.assertEqual(json_body['count'], 0)
        self.assertEqual(json_body['items'], [])

    def test_get_users_with_data(self):
        create_user()
        response = client.get('/users/')
        json_body = response.json()
        self.assertEqual(json_body['total'], 1)
        self.assertEqual(json_body['count'], 1)
        body = json_body['items'][0]
        self.assertIn('id', body)
        self.assertIn('buildings', body)
        self.assertEqual(mocked_user_body['document'], body['document'])

