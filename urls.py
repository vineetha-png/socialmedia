from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'dating'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('user_profile/<str:username>/', views.user_profile, name='user_profile'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('manage_request/<int:request_id>/', views.manage_request, name='manage_request'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('set_theme/', views.set_theme, name='set_theme'),
    path('send_connection_request/', views.send_connection_request, name='send_connection_request'),
    path('hide_user/', views.hide_user, name='hide_user'),
    path('get_messages/<str:username>/', views.get_messages, name='get_messages'),
    path('send_message/<str:username>/', views.send_message, name='send_message'),
    
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('edit_admin_profile/', views.edit_admin_profile, name='edit_admin_profile'),
    path('logout/', LogoutView.as_view(next_page='dating:admin_dashboard'), name='logout'),
    path('suspend_user/<int:user_id>/', views.suspend_user, name='suspend_user'),
    path('activate_user/<int:user_id>/', views.activate_user, name='activate_user'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('pin_post/<int:post_id>/', views.pin_post, name='pin_post'),
    path('unpin_post/<int:post_id>/', views.unpin_post, name='unpin_post'),
    path('archive_post/<int:post_id>/', views.archive_post, name='archive_post'),
    path('unarchive_post/<int:post_id>/', views.unarchive_post, name='unarchive_post'),
]