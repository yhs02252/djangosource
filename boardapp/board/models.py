from django.db import models
from django.contrib.auth.models import User

# 질문과 답변 게시판
# Question - pk(자동생성), 제목(title), 내용(content), 작성일시(created_at), 수정일시(modified_at, null=True, blank=True)
# Answer - pk(자동생성), 질문(외래키), 내용, 작성일시, 수정일시


class Question(models.Model):

    subject = models.CharField(max_length=50, verbose_name="제목")
    content = models.TextField(verbose_name="질문내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정일시")
    author = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)

    # 추천
    voter = models.ManyToManyField(
        User, related_name="voter_question", verbose_name="추천"
    )

    # 조회수
    viewcnt = models.IntegerField(verbose_name="조회수", default=0)

    class Meta:
        db_table = "questiontbl"

    def __str__(self):
        return self.subject


# 조회수 업데이트를 위한 모델
class QuestionCount(models.Model):
    ip = models.CharField(verbose_name="ip주소", max_length=30)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="질문"
    )

    def __unicode__(self):
        return self.ip


class Answer(models.Model):

    question = models.ForeignKey(
        Question, verbose_name="질문", on_delete=models.CASCADE
    )

    content = models.TextField(verbose_name="답변내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정일시")
    author = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)

    # 추천
    voter = models.ManyToManyField(
        User, related_name="voter_answer", verbose_name="추천"
    )

    class Meta:
        db_table = "answertbl"

    def __str__(self):
        return self.content


# 질문에 대한 댓글 : author, content, created_at, modified_at, question
# 답변에 대한 댓글 : author, content, created_at, modified_at, answer
class Comment(models.Model):

    content = models.TextField(verbose_name="댓글내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정일시")
    author = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    question = models.ForeignKey(
        Question, verbose_name="질문", on_delete=models.CASCADE, null=True, blank=True
    )
    answer = models.ForeignKey(
        Answer, verbose_name="답변", on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        db_table = "commenttbl"

    def __str__(self):
        return self.content
