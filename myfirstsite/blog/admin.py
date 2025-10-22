from django.contrib import admin
from .models import Category, Article, Author   , Tag       

class ArticleInline(admin.TabularInline):
    model = Article
    extra = 1

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")
    search_fields = ("name", "email")
    inlines = [ArticleInline]

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author")
    search_fields = ("title", "content")
    list_filter = ("author",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")  # чтобы видно было ID и название
    search_fields = ("name",)  
