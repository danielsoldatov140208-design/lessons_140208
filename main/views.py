from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
def base(request):
    return HttpResponse("главная страница моего сайта")\

def home(request):
    return HttpResponse("домашняя страница")

def about(request):
    return HttpResponse("Обо мне")

def contact(request):
    return HttpResponse("свяжитесь со мной")

class HelloView(View):
    def get(self, request):
        name = request.GET.get("name", "гость")
        return HttpResponse(f"Привет, {name}!")
    
def news_view(request):
    return render(request, 'news.html')

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