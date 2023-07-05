from django.urls import path
from book_collection import views as bkcln_v

urlpatterns = [
    path('fetch_books_wrap/', views.fetch_books_wrap, name='fetch_books_wrap')
]