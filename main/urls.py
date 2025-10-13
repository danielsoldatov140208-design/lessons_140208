from django.urls import path
from . import views  # импортируем views из той же папки

urlpatterns = [
    path('s', views.base, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('articles/', views.articles_view, name='articles'),
    path('', views.news_view, name='news'),
    path('home/', views.home, name='home'),
]
