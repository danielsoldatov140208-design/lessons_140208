from django.urls import path
from . import views  # импортируем views из той же папки

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('hello/', views.HelloView.as_view(), name='hello')
]
