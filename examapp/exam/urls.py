from django.urls import path
from .views import musician_create, musician_list, musician_edit
from .views import MusicianListView, MusicianDetailView, MusicianCreateView

urlpatterns = [
    # http://127.0.0.1:8000/exam/
    # http://127.0.0.1:8000/exam/musician/create/
    # 함수형 뷰 사용시
    # path("musician/list/", musician_list, name="musician_list"),
    path("musician/<int:id>/edit/", musician_edit, name="musician_edit"),
    # path("musician/create/", musician_create, name="musician_create"),
    # -------------------------------------------------------------------------------
    # 클래스 뷰 사용시
    path("musician/list/", MusicianListView.as_view(), name="musician_list"),
    # DetailView에서는 id를 자동으로 pk를 변환한 값으로 넣어줌
    path("musician/<int:pk>/", MusicianDetailView.as_view(), name="musician_detail"),
    path("musician/create/", MusicianCreateView.as_view(), name="musician_create"),
]
