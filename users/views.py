from django.conf import settings
import random
from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
from .models import VerificationOtp
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from django.template.loader import render_to_string
from rest_framework.response import Response
from decouple import config
from rest_framework import status

# Newly Added
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class Login(TokenObtainPairView):
    serializer_class = myTokenObtainPairSerializer


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"detail": "Logout successful."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST
            )


class Signup(APIView):
    template_name = "activation/activation_email.html"

    def post(self, request):
        serializer = User_Sign_Up(data=request.data)
        data = request.data
        if serializer.is_valid():
            user = serializer.save()
            user_otp = random.randint(100000, 999999)
            newOtp = VerificationOtp.objects.create(
                email=user.email, checkotp=user_otp)

            context = {
                "user": user,
                "otp": user_otp
            }
            email_html_message = render_to_string(
                "activation/activation_email.html", context
            )
            # Send the verification email
            subject = "IACHAT | Verification Your Account"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]
            send_mail(subject, email_html_message, f"No-Reply {from_email}",
                      recipient_list, html_message=email_html_message, fail_silently=True)
            # send_mail(
            #     subject,
            #     email_html_message,
            #     from_email,
            #     recipient_list,
            #     html_message=email_html_message,
            #     fail_silently=True,
            # )
            data = {"Text": "registered", "status": 200, "user": user.id}
            return Response(data=data)
        else:
            statusText = serializer.errors
            data = {"Text": statusText, "status": 404}
            return Response(data=data)


class OtpVerification(APIView):
    def post(self, request):
        userotp = int(request.data.get("otp"))
        User_Email = request.data.get("email")
        if userotp:
            if VerificationOtp.objects.filter(email=User_Email, checkotp=userotp):
                try:
                    verifyuser = User.objects.get(email=User_Email)
                    verifyuser.is_active = True
                    verifyuser.save()
                    Verification_otp_entries = VerificationOtp.objects.filter(
                        email=User_Email)
                    Verification_otp_entries.delete()
                    data = {"Text": "updated", "status": 200}
                    return Response(data=data)
                except:
                    data = {
                        "Text": "Entered wrong email",
                        "status": 400,
                    }
                    return Response(data=data)
            else:
                data = {
                    "Text": "Enterd wrong otp",
                    "email": User_Email,
                    "status": 400,
                }
                return Response(data=data)
        else:
            data = {
                "Text": "Enterd wrong otp",
                "email": User_Email,
                "status": 400,
            }
            return Response(data=data)
