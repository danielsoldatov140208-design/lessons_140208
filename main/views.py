from django.http import HttpResponse

def home(request):
    return HttpResponse("Привет! Это главная страница Django-проекта.")

def about(request):
    return HttpResponse("Обо мне")