# Loginify/urls.py
from django.urls import path
from . import views

urlpatterns = [
    
   # path('hello/', views.hello_world_view, name='hello_world'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('users/', views.list_all_users_view, name='list_users'),
    path('users/<str:email>/', views.get_user_details_by_email_view, name='get_user_by_email'),
    path('users/<str:email>/update/', views.update_user_details_view, name='update_user'),
    path('users/<str:email>/delete/', views.delete_user_view, name='delete_user'),




]