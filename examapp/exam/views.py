from django.shortcuts import render, redirect, get_object_or_404
from .forms import MusicianForm
from .models import Musician


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
