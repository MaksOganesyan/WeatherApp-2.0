from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('toggle-notifications/', views.toggle_notifications, name='toggle_notifications'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
