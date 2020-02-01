from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name='home' ),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_view ,name='register' ),
    path('update/register/', views.update_register ,name='register_update' ),
    path('change/password/', views.change_password_view ,name='change_password' ),
]