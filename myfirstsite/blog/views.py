from django.http import HttpResponse
from django.shortcuts import render
from .models import Book,Article
from .forms import BookForm, StudentForm
from django.db.models.functions import Length,Coalesce
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count,Func, Value

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

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():  
            form.save()         
            return redirect('books_view')
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books_view')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit.html', {'form': form, 'book': book})



def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('books_view')
    return render(request, 'confirm_delete.html', {'book': book})

def student_form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return HttpResponse(
                f"Форма успешно отправлена!<br>"
                f"Имя: {student.name}<br>"
                f"Возраст: {student.age}<br>"
                f"Email: {student.email}<br>"
                f"Группа: {student.group}"
            )
    else:
        form = StudentForm()

    return render(request, 'student_form.html', {'form': form})

def articles_view(request):
    articles = (
        Article.objects.annotate(content_length=Length('content'))
        .filter(content_length__gt=50)
        .order_by('-created_at')
    )
    total = articles.count()
    author_counts = (
        Article.objects.values('author')
        .annotate(count=Count('id'))
        .order_by('-count')
    )
    return render(request, 'articles.html', {
        'articles': articles,
        'total': total,
        'author_counts': author_counts
    })