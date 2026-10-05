from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Genre, Book
from .serializer import GenreSerializer, BookSerializer


class GenreListCreateAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
