from django.shortcuts import render, redirect, get_object_or_404
from board.models import Question
from board.forms import QuestionForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

################### 질문


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
