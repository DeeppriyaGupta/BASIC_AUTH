from django.urls import path
from user_app.views import Login_page, Register_page, Home_page, Logout_page

urlpatterns = [
    path('login/', Login_page, name='login-page'),
    path('register/', Register_page, name='register-page'),
    path('home/', Home_page, name='home-page'),
    path('logout/', Logout_page, name='logout')
]