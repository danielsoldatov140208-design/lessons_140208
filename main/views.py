from django.http import HttpResponse
from django.views import View
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
