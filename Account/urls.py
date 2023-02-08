from django.urls import path
from . import views

app_name = 'Account'
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user_login'),
]
