from django.urls import path
from .views.base_views import index, detail
from .views.question_views import create, modify, delete
from .views.answer_views import answer_create, answer_modify, answer_delete
from .views.comment_views import (
    comment_create_question,
    comment_modify_question,
    comment_delete_question,
    comment_create_answer,
    comment_modify_answer,
    comment_delete_answer,
)
from .views.vote_views import vote_question, vote_answer

app_name = "board"

urlpatterns = [
    # 추천
    path("question/vote/<int:id>/", vote_question, name="vote_question"),
    path("answer/vote/<int:id>/", vote_answer, name="vote_answer"),
    # 질문
    path("", index, name="index"),
    path("question/<int:id>/detail/", detail, name="detail"),
    path("question/create/", create, name="create"),
    path("question/<int:id>/modify", modify, name="modify"),
    path("question/<int:id>/delete", delete, name="delete"),
    # 답변
    path("answer/create/<int:id>/", answer_create, name="answer_create"),
    path("answer/modify/<int:id>/", answer_modify, name="answer_modify"),
    path("answer/delete/<int:id>/", answer_delete, name="answer_delete"),
    # 댓글
    path(
        "comment/create/question/<int:id>/",
        comment_create_question,
        name="comment_create_question",
    ),
    path(
        "comment/modify/question/<int:id>/",
        comment_modify_question,
        name="comment_modify_question",
    ),
    path(
        "comment/delete/question/<int:id>/",
        comment_delete_question,
        name="comment_delete_question",
    ),
    path(
        "comment/create/answer/<int:id>/",
        comment_create_answer,
        name="comment_create_answer",
    ),
    path(
        "comment/modify/answer/<int:id>/",
        comment_modify_answer,
        name="comment_modify_answer",
    ),
    path(
        "comment/delete/answer/<int:id>/",
        comment_delete_answer,
        name="comment_delete_answer",
    ),
]
