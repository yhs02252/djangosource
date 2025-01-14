from django.contrib import admin
from .models import Person, Post, Comment

# admin 사이트에서 관리할 모델 등록
# 1) admin.site.register(모델명) - 세부지정 불가능
admin.site.register(Person)


# 2)
# class PostAdmin(admin.ModelAdmin):
#     """
#     세부지정
#     """

#     pass


# admin.site.register(Post)


# 3) 2번 방식 개선
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # __str__ 기준으로 admin페이지에서 보여지는게 기본
    # list_display : 지정하면 __str__ 은 무시된다
    list_display = ("title", "author_name", "is_published", "created_at")
    list_display_links = ("author_name",)  # 조회로 들어갈 링크 컬럼 지정
    search_fields = ("title",)  # 검색 탭 추가


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "message", "created_at")
    list_display_links = ("message",)  # 조회로 들어갈 링크 컬럼 지정
