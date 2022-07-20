from django.contrib import admin
from .models import Category, Tag, Article, Thread, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'draft', 'account_role')


class ThreadAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'name', 'email')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'thread', 'name', 'email')
    search_fields = ('thread', 'publisher__name', 'authors__name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment, CommentAdmin)
