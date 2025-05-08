from rest_framework import viewsets, mixins

from .models import Book
from .serializers import BooksListSerializer


class BookViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Book.objects.all()
    serializer_class = BooksListSerializer
