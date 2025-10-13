from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
def home(request):
    return HttpResponse("главная страница моего сайта")

def about(request):
    return HttpResponse("Обо мне")

def contact(request):
    return HttpResponse("свяжитесь со мной")

class HelloView(View):
    def get(self, request):
        name = request.GET.get("name", "гость")
        return HttpResponse(f"Привет, {name}!")




def articles_view(request):
    articles = [
        {"title": "Django — основы", "author": "Артем"},
        {"title": "Шаблоны DTL", "author": "Мария"},
        {"title": "ORM в Django", "author": "Денис"},
    ]
    return render(request, 'articles.html', {'articles': articles})