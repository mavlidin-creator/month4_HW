from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.auth_login_view, name='login'),
    path('logout/', views.auth_logout_view, name='logout'),
    path('user_list/', views.user_list_view, name='user_list')
]