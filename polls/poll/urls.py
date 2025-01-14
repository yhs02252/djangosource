from django.urls import path
from . import views

# html에서 url 지정시 다른 앱과 이름 분리
app_name = "poll"

# path("경로", view, name="별칭")
# 뷰 - 1) 함수형 뷰 2) 클래스 뷰

urlpatterns = [
    # http://127.0.0.1:8000/admin/polls/
    path("", views.index, name="index"),
    # http://127.0.0.1:8000/admin/polls/1 : 1번 질문 조회
    path("<int:question_id>/", views.detail, name="detail"),
    # http://127.0.0.1:8000/admin/polls/1/vote : 1번 질문에 대한 답변 선택
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # http://127.0.0.1:8000/admin/polls/1/result : 투표 결과 보기
    path("<int:question_id>/result/", views.result, name="result"),
]
