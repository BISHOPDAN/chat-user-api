from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('token/', Login.as_view(), name='MyTokenObtainPairView'),
    path('signup/', Signup.as_view(), name='sign_up'),
    path('otpverification/', OtpVerification.as_view(), name='otpverification'),
    path('forgotpassword/', ForgotPassword.as_view(), name='forgotpassword'),
    path('verifyforgotemail/', VerifyForgotEmail.as_view(),
         name='verifyforgotemail'),
    path('updatepassword/', UpdatePassword.as_view(), name='updatepassword'),
    
    path('logout/',Logout.as_view(),name ='logout'),
    

]
