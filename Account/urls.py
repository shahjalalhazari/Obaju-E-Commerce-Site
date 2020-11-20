from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('activate/<uid>/<token>/', views.activate, name='activate'),
    path('login/', views.login_page, name='login'),
    path('user-login/', views.user_login, name='user_login'),
    path('logout/', views.logout_user, name='logout'),
    path("password_reset/", views.password_reset_request, name="password_reset")
]