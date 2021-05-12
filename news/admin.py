from django.contrib import admin
from . models import Article, ArticleImage


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageInline, ]


