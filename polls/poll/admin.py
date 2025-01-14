from django.contrib import admin
from .models import Question, Choice


# Question 안쪽에 Choice 직접 입력할 수 있게 만들기
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "created_at"]
    inlines = [ChoiceInline]


# @admin.register(Choice)
# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ["choice_text", "vote"]
