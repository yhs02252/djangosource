from django.db import models
from users.models import User
from taggit.managers import TaggableManager


# 번호(자동생성), user, 제목(title), 내용(content), image(option), 작성날짜(created_at), 수정날짜(modified_at)
class BlogPost(models.Model):

    user = models.ForeignKey(User, verbose_name="블로그 유저", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    # media/blog 폴더 사용
    image = models.ImageField(
        blank=True, null=True, upload_to="blogs", verbose_name="첨부파일"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="수정날짜")

    # 자동으로 별도의 테이블 생성
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    # 태그
    tag = TaggableManager(help_text="여러개의 태그를 원하시면 , 로 구분가능 합니다")

    class Meta:
        db_table = "blogtbl"

    def __str__(self):
        return self.title


# 댓글
# 원본글, 작성자, 내용, 작성일시, 수정일시
class Comment(models.Model):

    post = models.ForeignKey(BlogPost, verbose_name="원본글", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="수정날짜")

    class Meta:
        db_table = "commenttbl"

    def __str__(self):
        return f"{self.id}-{self.user}"
