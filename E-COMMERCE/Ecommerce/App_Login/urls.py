from django.urls import path
from App_Login import views

app_name = 'App_Login'

urlpatterns = [

    path('signup/', views.Sign_up, name='signup'),
    path('login/', views.Login_user, name='login'),
    path('logout/', views.Logout_user, name='logout'),
    path('profile/', views.User_profile, name='profile'),


]
