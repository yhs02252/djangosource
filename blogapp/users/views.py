from django.shortcuts import render, redirect
from .forms import UserForm


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user의 gender 요소가 비어있는지 확인
            # vaild 이후 검증이 끝난 form에서 gender를 색출하기 위해 cleaned_data를 사용
            if form.cleaned_data["gender"] == "":
                user.gender = 2
            # 이후 모델 save()
            user.save()
            return redirect("blogs:list")
    else:
        form = UserForm()
    return render(request, "users/register.html", {"form": form})
