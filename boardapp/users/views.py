from django.shortcuts import render, redirect
from django.contrib.auth import authenticate  # == loadUserByUsername (java)
from django.contrib.auth import login
from .forms import UserForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.models import User
from django.contrib import messages


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


# 비밀번호 초기화 view 생성
class CustomPasswordResetView(PasswordResetView):
    template_name = "users/password_reset_form.html"
    success_url = reverse_lazy("users:password_reset_done")
    email_template_name = "users/password_reset_email.txt"

    # 이메일이 있는지 없는지 확인 후 없으면 에러메세지 보여주기 / 이메일 존재 시 부모의 폼 유효성 호출
    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            messages.info(self.request, "입력하신 이메일을 확인해 주세요")
            return redirect("users:password_reset")
