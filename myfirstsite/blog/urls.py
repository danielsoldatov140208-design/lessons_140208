from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('books/', views.books_view, name='books_view'),]

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('books/', views.books_view, name='books_view'),
    path('search/', views.search_books, name='search_books'),
]
