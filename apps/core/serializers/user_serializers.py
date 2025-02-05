from rest_framework import serializers
from apps.core.models.user.user import User


class UserRegisterRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirmation_password = serializers.CharField(write_only=True)

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "email", "password"]

class UserBasicFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email"]
