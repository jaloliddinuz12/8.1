from django.urls import path

from .views import (
    GenreListCreateAPIView,
    GenreDetailAPIView,
    BookListCreateAPIView,
    BookDetailAPIView,
)

urlpatterns = [
    path('genre/', GenreListCreateAPIView.as_view()),
    path('genre/<int:pk>/', GenreDetailAPIView.as_view()),
    path('book/', BookListCreateAPIView.as_view()),
    path('book/<int:pk>/', BookDetailAPIView.as_view()),
]
