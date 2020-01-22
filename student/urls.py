from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.s_list, name='s_list'),
    path('create/', views.s_create, name='s_create'),
    path('search/', views.s_search, name='s_search'),
    path('detail/<int:roll_no>/', views.s_detail, name='s_detail'),
    path('edit/<int:roll_no>/', views.s_edit, name='s_edit'),
    path('delete/<int:s_id>', views.s_delete, name='s_delete'),
]