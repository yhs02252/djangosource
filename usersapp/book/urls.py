from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    # http://127.0.0.1:8000/books/
    path("", views.book_list, name="list"),
    # http://127.0.0.1:8000/books/1/
    path("<int:id>/", views.book_details, name="details"),
    # http://127.0.0.1:8000/books/1/edit/
    path("<int:id>/edit", views.book_edit, name="edit"),
    # http://127.0.0.1:8000/books/1/remove/
    path("<int:id>/remove", views.book_remove, name="remove"),
    # http://127.0.0.1:8000/books/create/
    path("create/", views.book_create, name="create"),
]
