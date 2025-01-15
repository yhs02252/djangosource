from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):

    # email 또한 필수요소로 지정
    email = forms.EmailField(label="이메일", help_text="사용중인 이메일을 입력하세요")

    class Meta:
        model = User
        # fields = "__all__"
        # 회원가입시 필요한 부분만 띄우기
        # password(비밀번호)는 default로 포함됨
        fields = ["username", "email"]
