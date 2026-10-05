from django.urls import path

from .views import (BookRetrieveAPIView, BookListAPIView)


urlpatterns = [
    path('book/', BookListAPIView.as_view()),
    path('book/genre/<int:course_id>/', BookListAPIView.as_view()),
    path('book/<int:genre_id>/', BookRetrieveAPIView.as_view()),
]