from django.contrib import admin
from .models import Category, Tag, Article, Request


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'draft', 'account_role')


class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'name', 'email')


class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Request, RequestAdmin)