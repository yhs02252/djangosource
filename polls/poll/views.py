from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView
from .models import Question, Choice

# 뷰(view)
# 1) 함수기반뷰(Function Base View : FBV)
# 2) 클래스기반뷰(Class Base View : CBV)
#   - Generic Display View : 많이 사용하는 뷰를 클래스로 작성
#       - 전체조회(ListView), 하나조회(DetailView)


# 함수형 뷰
# HttpResponse 객체 리턴 하거나 <- 단순한 값 밖에 넘겨주지 못함
# HttpResponse를 상속 받은 render()로 리턴 하거나
# redirect()로 리턴 필요

# 클래스 뷰
# TemplateView를 상속받아 경로로 이동


class HomeView(TemplateView):
    template_name = "home.html"


# def home(request):
#     return render(request, "home.html")


def index(request):
    # return HttpResponse("Hello")

    # 전체 question 조회
    questions = Question.objects.all()

    return render(request, "poll/index.html", {"questions": questions})


def detail(request, question_id):
    # get() : 원하는 정보를 찾지 못하는 경우 -> DoesNotExist error

    # 1)
    # try:
    #     question = Question.objects.get(id=question_id)
    # except:
    #     raise Http404("Question id를 확인해 주세요")

    # 2)
    question = get_object_or_404(Question, id=question_id)
    return render(request, "poll/detail.html", {"question": question})


def vote(request, question_id):
    # POST
    question = Question.objects.get(id=question_id)
    if request.method == "POST":
        # 사용자가 선택한 choice 가져오기
        selected_choice = request.POST.get("choice")  # choice id 가 넘어옴

        # choice 테이블에 가서 vote 한개 추가
        # choice 찾기
        # Choice.objects.get() or get_object_or_404(Choice, id=choice)
        choice = question.choice_set.get(id=selected_choice)
        choice.vote += 1
        choice.save()

        return redirect("poll:result", question_id)


def result(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, "poll/result.html", {"question": question})
