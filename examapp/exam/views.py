from django.shortcuts import render
from .forms import MusicianForm


def musician_create(request):
    form = MusicianForm()
    return render(request, "m_create.html", {"form": form})
