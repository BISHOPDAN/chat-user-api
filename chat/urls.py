# urls.py
from django.urls import path
from .views import ChatAPIView, TokenBalanceAPIView

urlpatterns = [
    path('aichat/', ChatAPIView.as_view(), name='chat'),
    path('balance/', TokenBalanceAPIView.as_view(), name='token-balance'),
]
