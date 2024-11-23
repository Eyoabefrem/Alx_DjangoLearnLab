from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    """
    A ViewSet for viewing and editing book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    """
    A ViewSet for viewing and editing book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
