from django.shortcuts import render
from .models import BlogPost


def blog_list(request):
    # 작성일자 내림차순
    posts = BlogPost.objects.order_by("created_at")

    return render(request, "blogs/list.html", {"posts": posts})
