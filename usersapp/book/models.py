from django.db import models


class Book(models.Model):

    # code, title, author, price, created_at
    code = models.IntegerField(
        verbose_name="도서코드",
        unique=True,
        help_text="코드는 숫자 5자리로 작성해주세요",
    )
    title = models.CharField(
        max_length=200, verbose_name="도서명", help_text="도서명은 공백일 수 없습니다"
    )
    author = models.CharField(max_length=100, verbose_name="저자")
    price = models.IntegerField(
        verbose_name="도서가격", help_text="가격은 최소 5000원 이상이어야 합니다"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록일시")

    class Meta:
        db_table = "booktbl"

    def __str__(self):
        return self.title
