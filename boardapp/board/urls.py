from django.urls import path
from .views import index, detail, answer_create, create, modify, delete

app_name = "board"

urlpatterns = [
    # 질문
    path("", index, name="index"),
    path("question/<int:id>/detail/", detail, name="detail"),
    path("question/create/", create, name="create"),
    path("question/<int:id>/modify", modify, name="modify"),
    path("question/<int:id>/delete", delete, name="delete"),
    # 답변
    path("answer/create/<int:id>/", answer_create, name="answer_create"),
]
