from django.contrib.auth.views import (LogoutView, LoginView, PasswordChangeView,
                                        PasswordResetView,PasswordResetDoneView, PasswordChangeDoneView, 
                                        PasswordResetConfirmView, PasswordResetCompleteView)
from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('exit/', views.logout ,name='exit'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('password-change/', PasswordChangeView.as_view(template_name='users/password_change_form.html'), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset_form.html'), name='password_reset_form'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_form'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]