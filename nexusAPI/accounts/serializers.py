from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "full_name", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            full_name=validated_data["full_name"],
            password=validated_data["password"],
        )
        return user

class StaffRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "full_name", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            full_name=validated_data["full_name"],
            password=validated_data["password"],
            is_staff=True,

        )
        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "full_name")
