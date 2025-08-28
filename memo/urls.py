from django.urls import path
from . import views

app_name = 'memo'

urlpatterns = [
    path('', views.home, name='home'),
    path('memo_list/', views.memo_list, name='memo_list'),
    path('memo_list_for_author/', views.memo_list_for_author, name='memo_list_for_author'),
    path('memo_create_row/', views.memo_create_row, name='memo_create_row'),
    path('<int:pk>/', views.memo_detail, name='memo_detail'),
    path('<int:pk>/update/', views.memo_update, name='memo_update'),
    path('<int:pk>/delete/', views.memo_delete, name='memo_delete')
]