from django.urls import path
from . import views

app_name = 'memo'

urlpatterns = [
    path('', views.home, name='home'),
    path('memo_list/', views.memo_list, name='memo_list'),
    path('memo_create_row/', views.memo_create_row, name='memo_create_row'),
    path('memo_detail/<int:pk>/', views.memo_detail, name='memo_detail'),
]