from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

class Tag(models.Model):
   name = models.CharField(max_length=30, unique=True)

def __str__(self):
       return self.name
   
class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name="Автор")
    tags = models.ManyToManyField(
    'Tag',
    blank=True,
    related_name='articles',
    verbose_name='Теги'
)


    def __str__(self):
        return self.title
    
class Author(models.Model):
    email = models.EmailField(verbose_name="Электронная почта автора")  
    name = models.CharField(max_length=100, verbose_name="Имя автора")

    def __str__(self):
        return self.name    

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    group = models.CharField(max_length=10)

    def __str__(self):
        return self.name