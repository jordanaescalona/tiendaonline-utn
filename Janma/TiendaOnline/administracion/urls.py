from django import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Index,Login

app_name = 'administracion'

urlpatterns = [
    path('',Index.as_view(),name="index"),
    path('login/',auth_views.LoginView.as_view(template_name='administracion/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='administracion/login.html'),name='logout'),
]