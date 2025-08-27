from django.contrib import admin
from .models import Memo

# Register your models here. -> 테이블을 등록하는 과정
@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'is_important', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('is_important', 'created_at', 'updated_at')
    ordering = ('-created_at',)