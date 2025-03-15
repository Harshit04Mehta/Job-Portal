from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.IndexPage, name="index"),
    path("signup/", views.SignupPage, name="signup"),
    path("register/", views.RegisterUser, name="register"),
    path("otp/", views.OTPPage, name="otp"),
    path("otpverify/", views.OTPVerify, name="otpverify"),
    path("loginpage/", views.LoginPage, name="loginpage"),
    path("login/", views.UserLogin, name="login"),
    path("profile/<int:pk>/", views.ProfilePage, name="profile"),
    path("updateprofile/<int:pk>/", views.UpdateProfile, name="updateprofile"),
    path("logout/", views.Logout, name="logout"),
]