from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name="Автор")

    def __str__(self):
        return self.title
    
class Author(models.Model):
    email = models.EmailField(verbose_name="Электронная почта автора")  
    name = models.CharField(max_length=100, verbose_name="Имя автора")
