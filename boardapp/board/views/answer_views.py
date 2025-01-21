from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from board.models import Question, Answer
from board.forms import AnswerForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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
            # return redirect("board:detail", id)
            return redirect(
                "{}#answer_{}".format(resolve_url("board:detail", id), answer.id)
            )
    else:
        form = AnswerForm()
    context = {"form": form, "question": question}
    return render(request, "board/question_detail.html", context)


def answer_modify(request, id):
    answer = get_object_or_404(Answer, id=id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            modified = form.save(commit=False)
            modified.modified_at = timezone.now()
            modified.save()
            # return redirect("board:detail", modified.question.id)
            return redirect(
                "{}#answer_{}".format(
                    resolve_url("board:detail", modified.question.id), modified.id
                )
            )
    else:
        form = AnswerForm(instance=answer)
    return render(request, "board/answer_modify.html", {"form": form, "id": id})


def answer_delete(request, id):
    answer = get_object_or_404(Answer, id=id)
    answer.delete()
    return redirect("board:detail", id=answer.question.id)
