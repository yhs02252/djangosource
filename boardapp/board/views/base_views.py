from django.shortcuts import render, redirect, get_object_or_404
from ..models import Question
from django.core.paginator import Paginator
from django.db.models import Q, Count

################### 질문


def index(request):

    # 띄울 페이지 지정
    page = request.GET.get("page", 1)

    # 검색
    keyword = request.GET.get("keyword", "")

    # 정렬기준
    so = request.GET.get("so", "")

    if so == "recommend":
        objects = Question.objects.annotate(num_voter=Count("voter")).order_by(
            "-num_voter", "-created_at"
        )
    elif so == "popular":
        objects = Question.objects.annotate(num_answer=Count("answer")).order_by(
            "-num_answer", "-created_at"
        )
    else:
        # 전체 질문 추출(작성일시 내림차순)
        objects = Question.objects.order_by("-created_at")

    # 검색어가 제목 or 내용 or 질문작성자 or 답변작성자에 포함된 경우 추출
    # or : Q 사용
    if keyword:
        objects = objects.filter(
            Q(subject__icontains=keyword)
            | Q(content__icontains=keyword)
            | Q(author__username__icontains=keyword)
            | Q(answer__author__username__icontains=keyword)
        ).distinct()

    # 한 페이지당 띄울요소 개수 지정
    paginator = Paginator(objects, 10)
    questions = paginator.get_page(page)
    max_page = len(paginator.page_range)

    context = {
        "questions": questions,
        "max_page": max_page,
        "page": page,
        "keyword": keyword,
        "so": so,
    }

    return render(request, "board/question_list.html", context)


def detail(request, id):

    question = get_object_or_404(Question, id=id)

    return render(request, "board/question_detail.html", {"question": question})
