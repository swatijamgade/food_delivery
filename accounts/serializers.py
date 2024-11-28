from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from .models import UserProfile


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password','phone']
        extra_kwargs = {'password': {'write_only': True}}


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class UpdatePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True)

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone', 'gender', 'date_of_birth','is_verified']

class UserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(source='userprofile.phone')
    gender = serializers.CharField(source='userprofile.gender')
    date_of_birth = serializers.CharField(source='userprofile.date_of_birth')
    is_verified = serializers.BooleanField(source='userprofile.is_verified', read_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone','gender', 'date_of_birth', 'is_verified']

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', required=True)
    last_name = serializers.CharField(source='user.last_name', required=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone', 'gender', 'date_of_birth', 'email']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user = instance.user
        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance