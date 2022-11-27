from django.contrib import admin
from articles.models import Article, Comment

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 10

class ArticleAdmin(admin.ModelAdmin):
    inlines =[
        CommentInLine,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)