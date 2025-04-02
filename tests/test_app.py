import unittest
from app import app

class TestStockHub(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_registro(self):
        response = self.client.post('/register', data={'modelo': 'X', 'serial': '123', 'cliente': 'João'})
        self.assertEqual(response.status_code, 200)

    def test_busca(self):
        response = self.client.get('/search?query=123')
        self.assertIn(b'123', response.data)

if __name__ == '__main__':
    unittest.main()