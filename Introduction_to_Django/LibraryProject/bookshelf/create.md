```python
from bookshelf.models import Book
Book = Book.objects.create(title="1984",author="George Orwell",publication_year = 1949)
Book
#<Book: 1984 by George Orwell>
```