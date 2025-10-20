from django.http import HttpResponse

def blog_home(request):
    return HttpResponse("Это блог-раздел моего сайта")
