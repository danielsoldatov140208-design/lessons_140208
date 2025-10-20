from django.urls import path
from . import views  

urlpatterns = [
    path('s', views.base, name='base'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('articles/', views.articles_view, name='articles'),
    path('', views.news_view, name='news'),
    path('home/', views.home, name='home'),
    path('students/', views.students_view, name='students'),
    path('login/', views.login, name='login'),
    path('article/<int:id>/', views.article, name='article'),
    path('user/<str:username>/', views.user, name='user'),
    path('article1/<int:id>/', views.article_detail, name='article_detail')
]
