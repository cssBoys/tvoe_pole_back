from django.contrib import admin
from .models import Category, PlaygroundType, Playground, PlaygroundImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(PlaygroundType)
class PlaygroundTypeAdmin(admin.ModelAdmin):
    pass


class PlaygroundImageInLine(admin.TabularInline):
    model = PlaygroundImage


@admin.register(Playground)
class PlaygroundAdmin(admin.ModelAdmin):
    inlines = [PlaygroundImageInLine, ]
