from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

def blog_home(request):
    return HttpResponse("Это блог-раздел моего сайта")

def books_view(request):
    expensive_books = Book.objects.filter(price__gt=2000)
    recent_books = Book.objects.filter(year__gt=2010).order_by('year')
    tolstoy_books = Book.objects.filter(author__icontains='Толстой')

    context = {
        'expensive_books': expensive_books,
        'recent_books': recent_books,
        'tolstoy_books': tolstoy_books,
    }

    return render(request, 'book.html', context)

def search_books(request):
    query = request.GET.get('q')  
    results = []

    if query: 
        results = Book.objects.filter(author__icontains=query)

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search.html', context)