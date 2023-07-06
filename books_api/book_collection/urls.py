from django.urls import path
from book_collection import views as bkcln_v

urlpatterns = [
    path('fetch_books_wrap/', bkcln_v.fetch_books_wrap, name='fetch_books_wrap'),
    path('get_all_books/', bkcln_v.get_all_books, name='get_all_books'),
    # path('get_all_books_auth/', bkcln_v.get_all_books_auth, name='get_all_books_auth'),
    path('book_create/', bkcln_v.book_create, name='book_create'),
    path('book_retrieve/', bkcln_v.book_retrieve, name='book_retrieve'),
    path('book_update/', bkcln_v.book_update, name='book_update'),
    path('book_delete/', bkcln_v.book_delete, name='book_delete'),
]