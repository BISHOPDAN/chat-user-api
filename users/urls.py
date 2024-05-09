from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('login/', Login.as_view(), name='MyTokenObtainPairView'),
    path('signup/', Signup.as_view(), name='sign_up'),
    path('otpverification/', OtpVerification.as_view(), name='otpverification'),
    
    path('logout/',Logout.as_view(),name ='logout'),
    

]
