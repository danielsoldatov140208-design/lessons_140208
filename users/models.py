from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.first_name} {self.last_name}"

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    title = models.CharField(max_length=100)                    
    content = models.TextField()                                 
    created_at = models.DateTimeField(auto_now_add=True)         

    def __str__(self):
        return self.title
