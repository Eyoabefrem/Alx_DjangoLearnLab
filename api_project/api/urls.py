from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Initialize the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# URL patterns
urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for CRUD operations
    path('', include(router.urls)),  # Automatically adds routes for BookViewSet
]

from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    ...,
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
