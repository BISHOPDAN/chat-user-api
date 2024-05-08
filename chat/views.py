from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Chat
from .serializers import ChatSerializer
from users.serializers import userDataSerializer
from rest_framework.permissions import IsAuthenticated
import random



def generate_ai_response(user_message):
    # Check for specific user messages
    if user_message.lower() == "hello, chatbot!":
        # Response for greeting
        return "Hello! Welcome to our service. How can I assist you today?"
    elif 'i need some help!' in user_message.lower():
        # Response for requesting help
        return "Thank you for reaching out for help. Please wait for a moment, and we'll attend to you shortly."
    else:
        # Generic responses
        responses = [
            "I'm not sure I understand.",
            "Let's change the topic for a moment.",
            "That's intriguing!",
            "I appreciate your message!",
            "Could you please elaborate?"
        ]

        # Select a generic response randomly
        return random.choice(responses)



class ChatAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChatSerializer(data=request.data)

        if serializer.is_valid():
            user_email = request.data.get('email')
            user_message = serializer.validated_data.get('message')
            user = User.objects.filter(email=user_email).first()

            if user:
                if user.tokens >= 100:
                    user.tokens -= 100
                    user.save()
                    response = generate_ai_response(user_message)
                    chat = Chat.objects.create(user=user, message=user_message, response=response)
                    return JsonResponse({'response': response, 'tokens_remaining': user.tokens})
                else:
                    return Response({'error': 'Insufficient tokens'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TokenBalanceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_email = request.data.get('email')
        user = User.objects.filter(email=user_email).first()
        if user:
            return JsonResponse({'tokens_remaining': user.tokens})
        return Response({'error': 'Invalid email'}, status=status.HTTP_401_UNAUTHORIZED)
