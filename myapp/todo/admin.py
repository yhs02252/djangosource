from django.contrib import admin
from .models import Todo

# admin 페이지에서 Todo 모델 작업 수행
admin.site.register(Todo)
