from django.urls import path
from . import views

app_name = 'memo'

urlpatterns = [
    path('', views.home, name='home'),
    path('memo_list/', views.memo_list, name='memo_list'),
]