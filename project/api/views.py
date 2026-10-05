from django.shortcuts import render

from rest_framework.generics import ( ListCreateAPIView,RetrieveUpdateDestroyAPIView)

from rest_framework import permissions
from .models import Genre, Book
from .serializer import BookSerializer

class BookListAPIView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        genre_id = self.kwargs.get("genre_id")
        if genre_id:
            book = Genre.objects.filter(genre_id=genre_id)
        else:
            book = Genre.objects.all()
        return book


    def get_serializer_class(self):
        # if self.request.user.is_staff:
        #     return BookSerializerForAdmin
        return BookSerializer


class BookRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"
    lookup_url_kwarg = "student_id"
    permission_classes = [permissions.IsAdminUser]



