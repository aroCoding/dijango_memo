from django.shortcuts import render
from .models import Memo

# Create your views here.
def home(request):
    return render(request=request, template_name='memo/home.html')

def memo_list(request):
    return render(request=request, template_name='memo/memo_list.html', context={ 'memos': Memo.objects.all() })