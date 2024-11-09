from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    for book in books:
        print(f"Title: {book.title}, Author: {book.author.name}")

def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(f"Title: {book.title}, Library: {library.name}")

def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"Librarian: {librarian.name}, Library: {library.name}")

if __name__ == "__main__":
    # Replace 'Author Name' and 'Library Name' with actual names in your database
    books_by_author('Author Name')
    books_in_library('Library Name')
    librarian_for_library('Library Name')
