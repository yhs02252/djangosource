from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    # http://127.0.0.1:8000/blogs/
    path("", views.blog_list, name="list"),
    # http://127.0.0.1:8000/blogs/8/
    path("<int:pk>/", views.blog_detail, name="detail"),
    # http://127.0.0.1:8000/blogs/create/
    path("create/", views.blog_create, name="create"),
    # http://127.0.0.1:8000/blogs/8/update/
    path("<int:pk>/update/", views.blog_update, name="update"),
    # http://127.0.0.1:8000/blogs/8/delete/
    path("<int:pk>/delete/", views.blog_delete, name="delete"),
    # http://127.0.0.1:8000/blogs/comment/create/
    path("comment/create/", views.comment_create, name="comment_create"),
    # http://127.0.0.1:8000/blogs/8/post/like/
    path("<int:pk>/post/like/", views.post_like, name="post_like"),
]
