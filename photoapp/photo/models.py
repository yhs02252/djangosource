from django.db import models

# 문자열 저장
# CharField(length 지정 필요) : 짧은 문자열 저장
# TextField() : 좀 더 긴 문자열 저장


class Photo(models.Model):
    title = models.CharField(max_length=50)
    auther = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
