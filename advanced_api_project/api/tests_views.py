from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpassword")

        # Create test data
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.author
        )

        # Endpoints for testing
        self.list_url = '/books/'
        self.detail_url = f'/books/{self.book.id}/'
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Harry Potter", response.data[0]["title"])
    def test_create_book(self):
        self.client.login(username="testuser", password="testpassword")  # Authenticate
        data = {
            "title": "Harry Potter and the Chamber of Secrets",
            "publication_year": 1998,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.last().title, "Harry Potter and the Chamber of Secrets")
    def test_update_book(self):
        self.client.login(username="testuser", password="testpassword")  # Authenticate
        data = {"title": "Harry Potter and the Sorcerer's Stone"}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Harry Potter and the Sorcerer's Stone")
    def test_delete_book(self):
        self.client.login(username="testuser", password="testpassword")  # Authenticate
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url, {"author": self.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Harry Potter", response.data[0]["title"])
    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Harry"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Harry Potter", response.data[0]["title"])
    def test_order_books_by_publication_year(self):
        Book.objects.create(
            title="Harry Potter and the Chamber of Secrets",
            publication_year=1998,
            author=self.author
        )
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["publication_year"], 1997)
    def test_unauthenticated_user_access(self):
        response = self.client.post(self.list_url, {"title": "Unauthorized Book"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    def test_authenticated_user_access(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(self.list_url, {"title": "Authorized Book"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
