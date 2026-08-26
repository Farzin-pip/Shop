from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='user_register'),
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('register/verify/', views.UserRegisterVerifyCodeView.as_view(), name='verify_code'),
    path('login/verify/', views.UserLoginVerifyCodeView.as_view(), name='login_verify'),
    path('logout/', views.UserLogout.as_view(), name='user_logout'),
]