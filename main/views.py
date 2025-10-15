from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
def base(request):
    return HttpResponse("главная страница моего сайта")\

def home(request):
    return render(request, "home.html")

def about(request):
    return HttpResponse("Обо мне")

def contact(request):
    return HttpResponse("свяжитесь со мной")

class HelloView(View):
    def get(self, request):
        name = request.GET.get("name", "гость")
        return HttpResponse(f"Привет, {name}!")
    

def news_view(request):
    news = [
        {"title": "Django 5.0 вышел!", "text": "Вышла новая версия Django."},
        {"title": "Python 3.13", "text": "Добавлены новые возможности!"},
    ]
    return render(request, 'news.html', {'news': news})


def articles_view(request):
    articles = [
        {"title": "Django — основы", "author": "Артем"},
        {"title": "Шаблоны DTL", "author": "Мария"},
        {"title": "ORM в Django", "author": "Денис"},
    ]
    return render(request, 'articles.html', {'articles': articles})

def students_view(request):
    students = [
        {"name": "Айжан", "age": 19, "group": "IT-23A"},
        {"name": "Мансур", "age": 20, "group": "IT-23A"},
        {"name": "Алихан", "age": 18, "group": "IT-23B"},
    ]

    group_info = {
        "name": "IT-23A",
        "specialty": "Веб-разработка",
        "year": 2025
    }

    context = {
        'students': students,
        'group_info': group_info
    }

    return render(request, 'students.html', context)


def login(request):
    response = None
    if request.method == 'POST':
        username = request.POST.get('name')
        message = request.POST.get('message')
        if username=="" or message=="":
            response = "Пожалуйста, заполните все поля."
        else:
            response = f"Привет {username}, Твое сообщение получено: {message}"
    return render(request, 'login.html', {'response': response})

def article(request, article_id):
    return HttpResponse(f"Вы просматриваете статью с номером:{article_id}.")
