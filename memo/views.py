from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo
from .form import MemoForm
from django.contrib import messages
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
    return render(request=request, template_name='memo/memo_form.html', context={ 'form': form })

def memo_detail(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    return render(request=request, template_name='memo/memo_detail.html', context={ 'memo': memo })


def memo_update(request, pk):

    memo = get_object_or_404(Memo, pk=pk)

    if request.method == 'POST':
        form = MemoForm(request.POST, instance=memo)
        
        if form.is_valid():
            form.save()
            return redirect('memo:memo_detail', pk=pk)

    else:
        form = MemoForm(instance=memo)

    return render(request=request, template_name='memo/memo_form.html', context={ 'form': form, 'title': '메모 수정' })

def memo_delete(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    
    if request.method == 'POST':
        memo.delete()
        return redirect('memo:memo_list')
        
    else:
        messages.error(request, '메모 삭제에 실패했습니다.')
        return redirect('memo:memo_detail', pk=pk)
