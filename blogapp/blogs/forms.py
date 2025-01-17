from django import forms
from .models import BlogPost


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        # 모델에서 사용할 필드 지정
        # 방법 1 : 전부 가져오고 제외시킬 요소 지정
        # fields = "__all__"
        # exclude_field = {"created_at", "modified_at"}

        # 방법2 : 가져올 요소만 지정
        fields = ["title", "content", "image", "tag"]
