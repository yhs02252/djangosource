from django.db import models
from django.contrib.auth.models import (
    User,
    PermissionsMixin,
    AbstractUser,
    BaseUserManager,
)
from django.contrib.auth.base_user import AbstractBaseUser

# User작동 원리
# AbstractBaseUser : password, last_login 필드만 가지고있음
# -> AbstractUser : is_superuser, groups, user_permissions 필드 소유
#  -> User

# User 모델에 다른 필드를 추가하고 싶다면
# class CustomaUser(User):
# 필드 추가 지정


class UserManager(BaseUserManager):
    def _create_user(self, email, password, name, gender=2, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(
            email=email, password=password, name=name, gender=gender, **extra_fields
        )
        # 비밀번호 암호화
        user.set_password(password)
        user.save(using=self._db)

    def create_user(self, email, password, name, gender, **extra_fields):
        # 일반 유저 계정 생성 시 호출되는 메소드
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_staff", False)
        return self._create_user(email, password, name, gender, **extra_fields)

    def create_superuser(self, email, password, name, **extra_fields):
        # admin 계정 생성 시 호출되는 메소드
        # 장고 필수 설정 옵션
        # is_staff, is_superuser
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        return self._create_user(email, password, name, **extra_fields)


# User를 직접 지정하는 방식
# email을 id 방식으로 받기(username 개념)
# 성별, 이름, 비밀번호
class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [
        (0, "남자"),
        (1, "여자"),
        (2, "비공개"),
    ]

    email = models.EmailField(verbose_name="이메일", unique=True, max_length=255)
    name = models.CharField(verbose_name="이름", max_length=50)
    gender = models.SmallIntegerField(
        verbose_name="성별", choices=GENDER_CHOICES, blank=True
    )
    is_staff = models.BooleanField(verbose_name="스태프", default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email
