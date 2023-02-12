from django.urls import path
from . import views

app_name = 'Account'
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('otplogin/', views.OtoLoginView.as_view(), name='user_register'),
    path('otpcheck/', views.CheckOtpView.as_view(), name='check_otp'),
]
