from django.urls import path
from book_collection import views as bkcln_v

urlpatterns = [
    path('fetch_books_wrap/', bkcln_v.fetch_books_wrap, name='fetch_books_wrap'),
    path('get_all_books/', bkcln_v.get_all_books, name='get_all_books'),
]