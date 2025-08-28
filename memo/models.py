from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Memo(models.Model):

    # 작성자 추가 (ForeignKey)
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='memos', #user.memos.all()로 접근 가능
        verbose_name='작성자' #admin 페이지에서 보여지는 이름
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    is_important = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # print 시 참조값이 아닌 Memo.title 값을 반환
    def __str__(self):
        return self.title