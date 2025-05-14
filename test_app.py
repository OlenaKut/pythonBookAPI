import unittest
from app import app

class SimpleApiTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_route(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

    def test_books_get(self):
        res = self.client.get("/books")
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.get_json(), list)

    def test_create_book(self):
        res = self.client.post("/books", json={
            "title": "Testbok",
            "author": "Olena",
            "year": 2023
        })
        self.assertEqual(res.status_code, 201)
        self.assertIn("title", res.get_json())

if __name__ == '__main__':
    unittest.main()
