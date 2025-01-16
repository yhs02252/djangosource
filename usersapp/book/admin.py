from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # admin page 리스트에서 보여질 부분
    list_display = ("code", "title", "author")
