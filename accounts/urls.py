from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.user_login, name='login'),
    path('accounts/logout/', views.logout, name='logout')
]