from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class User_Sign_Up(ModelSerializer):
    password2 = serializers.CharField(
        style={"input_type": "passsword"}, write_only=True
    )

    class Meta:
        model = User
        fields = "__all__"

    def save(self):
        user = User(
            username=self._validated_data["username"],
            phone_number=self._validated_data["phone_number"],
            email=self._validated_data["email"],
            password=self._validated_data["password"],
            is_active=False,
        )
        password = self._validated_data["password"]
        password2 = self._validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError(
                {"password": "password does not match"})
        user.set_password(password)
        user.save()
        return user


class myTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["user_pk"] = user.id
        token["email"] = user.email
        token["is_active"] = user.is_active
        token["is_superuser"] = user.is_superuser
        return token


class userDataSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "is_superuser",
            "phone_number",
            "is_active",
        ]
