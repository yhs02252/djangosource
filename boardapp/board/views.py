from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils import timezone

################### 질문


def index(request):

    # 띄울 페이지 지정
    page = request.GET.get("page", 1)

    # 전체 질문 추출(작성일시 내림차순)
    objects = Question.objects.order_by("created_at")

    # 한 페이지당 띄울요소 개수 지정
    paginator = Paginator(objects, 10)
    questions = paginator.get_page(page)

    return render(request, "board/question_list.html", {"questions": questions})


def detail(request, id):

    question = get_object_or_404(Question, id=id)

    return render(request, "board/question_detail.html", {"question": question})


@login_required(login_url="users:login")
def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect("board:detail", id=question.id)
    else:
        form = QuestionForm()

    return render(request, "board/question_form.html", {"form": form})


def modify(request, id):
    question = get_object_or_404(Question, id=id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            modified = form.save(commit=False)
            modified.modified_at = timezone.now()
            modified.save()
            return redirect("board:detail", id=id)
    else:
        form = QuestionForm(instance=question)
    return render(request, "board/question_modify.html", {"form": form, "id": id})


def delete(request, id):
    question = Question.objects.get(id=id)
    question.delete()
    return redirect("board:index")


################### 답변


@login_required(login_url="users:login")
def answer_create(request, id):

    question = get_object_or_404(Question, id=id)

    # model 이용
    # content = request.POST.get("content")

    # # 방법 1
    # answer = Answer(content=content, question=question)
    # answer.save()

    # # 방법 2
    # Answer.objects.create(content=content, question=question)

    # 방법 3
    # question.answer_set.create(content=content)
    # return redirect("board:detail", id=id)

    # form 사용
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            # form.save() Question 정보 없음
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect("board:detail", id)
    else:
        form = AnswerForm()
    context = {"form": form, "question": question}
    return render(request, "board/question_detail.html", context)
