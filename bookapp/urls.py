from django.urls import path
from .views import *

urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('book_create/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>', BookRetrieveUpdateDestroyView.as_view()),
    path('category/', BookCategoryListView.as_view(), name='category'),
    path('category/<int:pk>/', BookCategoryRetrieveAPIView.as_view(), name='category_id'),
    path('author/', AuthorListView.as_view(), name='author'),
    path('author/<int:pk>/', AuthorRetrieveAPIView.as_view(), name='author_id'),

    path('mybooks/', MyBookListView.as_view(), name='mybook')
]
