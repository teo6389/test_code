from django.test import TestCase
from book_collection import views

class BookCollectionTest(TestCase):
    
    def test_url_reponse(self):
        response = self.client.get("/books/get_all_books/")
        self.assertEqual(response.status_code, 200)

    def test_get_books_reponse(self):
        self.assertIsNotNone(views.get_books({}))
        # self.assertTrue(views.get_books({}) is True)