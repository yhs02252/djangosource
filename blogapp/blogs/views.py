from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator

# login_required : 로그인 여부 확인 후 실행
# 로그인이 안되어 있을 시 로그인 페이지로 이동시켜줌
# login_url= 을 지정하지 않으면 django기본 경로로 이동(네임스페이스 사용가능)


@login_required(login_url="users:login")
def comment_create(request):
    if request.method == "POST":
        content = request.POST.get("content").strip()
        post_pk = request.POST.get("post_pk").strip()

        post = get_object_or_404(BlogPost, pk=post_pk)

        if content and post_pk:
            # comment 생성
            # 1) 객체 생성
            # comment = Comment(post=post,user=request.user,content=content)
            # comment.save()

            # 2) objects.create 이용
            comment = Comment.objects.create(
                post=post, user=request.user, content=content
            )
            return redirect("blogs:detail", pk=comment.post.pk)

        # 댓글이 안들어올시 에러처리
        messages.error(request, "댓글을 입력해 주세요")
        return redirect("blogs:detail", pk=post_pk)


def blog_delete(request, pk):
    post = BlogPost.objects.get(id=pk)
    post.delete()
    return redirect("blogs:list")


def blog_update(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if request.method == "POST":

        form = BlogForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect("blogs:detail", pk=pk)

    else:
        form = BlogForm(instance=post)

    return render(request, "blogs/update.html", {"form": form, "pk": pk})


def blog_create(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # 작성자(== 로그인 사용자)
            post.user = request.user
            post.save()
            form.save_m2m()
            return redirect("blogs:list")

    else:
        form = BlogForm()

    return render(request, "blogs/create.html", {"form": form})


def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    # 현재 로그인한 유저가 게시물에 좋아요를 누른 상태 확인
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    return render(request, "blogs/detail.html", {"post": post, "is_liked": is_liked})


def blog_list(request):

    # request.POST.get()
    page = request.GET.get("page", 1)

    # 작성일자 내림차순
    post = BlogPost.objects.order_by("created_at")

    paginator = Paginator(post, 10)
    posts = paginator.get_page(page)

    return render(request, "blogs/list.html", {"posts": posts, "page": page})


def post_like(request, pk):

    # post.pk, userid 필요
    post = get_object_or_404(BlogPost, pk=pk)
    is_liked = post.likes.filter(id=request.user.id).exists()
    if is_liked:
        # 좋아요 상태에서 클릭 요청이 들어오면 유저정보 삭제
        post.likes.remove(request.user)
        # 빈 하트를 위해 False값 입력
        is_liked = False
    else:
        # 좋아요가 아닌 상태에서 클릭 요청이 들어오면 유저정보 추가
        post.likes.add(request.user)
        # 채워진 하트를 위해 False값 입력
        is_liked = True

    # 기존 방식은 HttpResponse
    return JsonResponse({"likes_count": post.likes.count(), "is_liked": is_liked})
