from django import forms
from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        # field에 전부 포함
        fields = "__all__"
        # field 요소에 created_at 제외
        exclude_fields = ["created_at"]
