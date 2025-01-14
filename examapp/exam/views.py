from django.shortcuts import render, redirect, get_object_or_404
from .forms import MusicianForm
from .models import Musician
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy


# 뷰(view)
# 1) 함수기반뷰(Function Base View : FBV)
# 2) 클래스기반뷰(Class Base View : CBV)
#   - Generic Display View : 많이 사용하는 뷰를 클래스로 작성
#       - 전체조회(ListView), 한개조회(DetailView), 수정(UpdateView), 삭제(DeleteView), 삽입(CreateView)


######################################## 클래스기반 뷰
class MusicianListView(ListView):
    model = Musician
    template_name = "exam/m_list.html"
    # 데이터 추출 후 사용하는 이름은 소문자모델명_list(기본)
    context_object_name = "musicians"


class MusicianDetailView(DetailView):
    model = Musician
    template_name = "exam/m_detail.html"
    # 데이터 추출 후 사용하는 이름은 object
    context_object_name = "musician"


class MusicianCreateView(CreateView):
    template_name = "exam/m_create.html"
    form_class = MusicianForm
    # url 지정 시 name을 이용한 지정시 reverse() or reverse_lazy()
    success_url = reverse_lazy("musician_list")


######################################## 함수기반 뷰


def musician_edit(request, id):

    # musician = Musician.objects.get(id=id)
    musician = get_object_or_404(Musician, id=id)

    if request.method == "POST":
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect("musician_list")
    else:
        form = MusicianForm(instance=musician)

    return render(request, "exam/m_edit.html", {"form": form})


def home(request):
    return render(request, "home.html")


def musician_list(request):

    musicians = Musician.objects.all()

    return render(request, "exam/m_list.html", {"musicians": musicians})


def musician_create(request):

    if request.method == "POST":
        # == 스프링에서 DTO 에 담는것과 같은 개념
        form = MusicianForm(request.POST)
        # 유효성 검증
        if form.is_valid():
            form.save()  # model에 save를 거는것과 같은 효과
            return redirect("musician_list")
    else:
        form = MusicianForm

    return render(request, "exam/m_create.html", {"form": form})
