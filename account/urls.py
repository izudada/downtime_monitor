from django.urls import path
from . import views


urlpatterns = [
    path('auth/register/', views.register, name="register"),
    path('auth/login/', views.login_user, name="login"),
]