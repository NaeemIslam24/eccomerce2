from . import views
from django.urls import path
from django.contrib.auth import views as auth_view



urlpatterns = [
    path('', views.login_register, name='login_register'),
    path('logout', views.logoutuser, name='logout'), 
    path('test', views.test, name='test'), 

    # password reset start
    path('reset_pass/', auth_view.PasswordResetView.as_view(
        template_name='account/password_reset.html'), name="reset_password"),
    path('reset_pass_sent/', auth_view.PasswordResetDoneView.as_view(template_name='account/password_reset_sent.html'),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='account/reset.html'),
         name="password_reset_confirm"),
    path('reset_pass_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='account/reset_complete.html'),
         name="password_reset_complete"),
    # password reset send 

]

