from django.shortcuts import render, redirect
from django.contrib.auth import authenticate  # == loadUserByUsername (java)
from django.contrib.auth import login, logout
from .forms import UserForm


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # 로그인 처리
            # username, password 가져오기
            username = form.cleaned_data.get("username")  # dict 구조라서 [] 사용 가능
            password = form.cleaned_data.get("password1")  # html에 name과 맞춰야함

            # DB 정보와 일치 한다면 인증받은 객체 user 리턴
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # 세션에 user 정보 담기

            return redirect("board:index")
    else:
        form = UserForm()

    return render(request, "users/register.html", {"form": form})
