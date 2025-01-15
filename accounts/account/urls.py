from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_view
from . import views

# app_name을 지정하지 않고 django의 로그인,로그아웃,비번변경,비번초기화 사용하는 방법

urlpatterns = [
    path(
        "login/",
        auth_view.LoginView.as_view(template_name="account/login.html"),
        name="login",
    ),
    path("logout/", auth_view.LogoutView.as_view(), name="logout"),
    # 비밀번호 변경시 템플릿만 변경
    # path(
    #     "password_change/",
    #     auth_view.PasswordChangeView.as_view(
    #         template_name="account/password_change.html"
    #     ),
    #     name="password_change",
    # ),
    # path(
    #     "password_change/done/",
    #     auth_view.PasswordChangeDoneView.as_view(
    #         template_name="account/password_change_done.html"
    #     ),
    #     name="password_change_done",
    # ),
    # 비밀번호 변경 시 템플릿 변경 + 이동하는 경로 변경
    path(
        "password_change/",
        auth_view.PasswordChangeView.as_view(
            template_name="account/password_change.html",
            success_url=reverse_lazy("home"),
        ),
        name="password_change",
    ),
    # 비밀번호 초기화
    path(
        "password_reset/",
        views.CustomPasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_view.PasswordResetDoneView.as_view(
            template_name="account/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_view.PasswordResetConfirmView.as_view(
            template_name="account/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_view.PasswordResetCompleteView.as_view(
            template_name="account/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    # 회원가입
    path("register/", views.users_register, name="register"),
]
