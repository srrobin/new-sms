from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.t_list, name='t_list'),
    path('create/', views.t_create, name='t_create'),
    path('edit/<int:t_id>', views.t_edit, name='t_edit'),
    path('delete/<int:t_id>', views.t_delete, name='t_delete'),
]