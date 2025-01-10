from django.urls import path
from .views import photo_list, photo_edit, photo_detail, photo_post, photo_remove

urlpatterns = [
    # http://127.0.0.1:8000/photo 리스트
    path("", photo_list, name="photo_list"),
    # http://127.0.0.1:8000/photo/1 조회
    path("<int:id>/", photo_detail, name="photo_detail"),
    # http://127.0.0.1:8000/photo/1/edit 수정
    path("<int:id>/edit/", photo_edit, name="photo_edit"),
    # http://127.0.0.1:8000/photo/new 등록
    path("new/", photo_post, name="photo_post"),
    # http://127.0.0.1:8000/photo/1/remove 삭제
    path("<int:id>/remove/", photo_remove, name="photo_remove"),
]
