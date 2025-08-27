from django.shortcuts import render, redirect
from .models import Memo
from .form import MemoForm
# Create your views here.
def home(request):
    return render(request=request, template_name='memo/home.html')

def memo_list(request):
    return render(request=request, template_name='memo/memo_list.html', context={ 'memos': Memo.objects.all() })

def memo_create_row(request):

    if request.method == 'POST':
        form = MemoForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            is_important = form.cleaned_data['is_important']

            # DB에 저장
            Memo.objects.create(title=title, content=content, is_important=is_important)
            return redirect('memo:memo_list')

    # GET 요청 시 빈 폼 생성
    else:
        form = MemoForm()

    # GET 요청이거나 폼이 유효하지 않을 때
    return render(request=request, template_name='memo/memo_create.html', context={ 'form': form })