from rest_framework import serializers
from .models import Author, Book
from datetime import date

# serializers.py

"""
Serializers for the Author and Book models.
- BookSerializer ensures data integrity (e.g., no future publication years).
- AuthorSerializer dynamically includes nested books using BookSerializer.
"""

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes the Book model, ensuring that publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model, including a nested serialization of their books.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']