from django.contrib import admin
from .models import BlogPost, Comment


@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "created_at"]
