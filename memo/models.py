from django.db import models

# Create your models here.
class Memo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_important = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # print 시 참조값이 아닌 Memo.title 값을 반환
    def __str__(self):
        return self.title