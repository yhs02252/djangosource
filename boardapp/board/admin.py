from django.contrib import admin
from .models import Question, Answer


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 2


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("subject", "created_at")
    search_fields = ["subject"]
    inlines = [AnswerInline]
