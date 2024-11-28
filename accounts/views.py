from rest_framework import status
from rest_framework .response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, LoginSerializer, UpdatePasswordSerializer, ResetPasswordSerializer, ProfileSerializer, UserSerializer, UserProfileUpdateSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message : User registered succesfully'}, staus=status.HTTP_200_OK)
        return Response({'message : Resgistration failed'}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid:
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)
            if user is None:
                return Response({'message : Login succesfully'}, status=status.HTTP_200_OK)
            return Response({'message : Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED )
        return Response({'message : Login failed'}, status=status.HTTP_400_BAD_REQUEST)

class UpdatePasswordView(APIView):

    def put(self, request):
        serializer = UpdatePasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message = Password updated successfully'}, status=status.HTTP_200_OK)
        return Response({'error : Error'}, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):

    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message : Passowrd rest successfully'}, status=status.HTTP_200_OK)
        return Response({'error : Error'}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    def get(self, request):
        user = request.user
        profile = UserProfileView.object.get(user=user)
        return Response({'message : User profile retrived successfully'}, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        profile = UserProfileView.object.get(user=user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message : Profile updated successfully'}, status=status.HTTP_200_OK)
        return Response({'message : Failed to update profile'}, staus=status.HTTP_400_BAD_REQUEST)

class UserProfileUpdateView(APIView):

    def put(self, request):
        profile = request.user.profile
        serializer = UserProfileUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message : Profile updated successfully'}, status=status.HTTP_200_OK)
        return Response({'error : Error'}, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(data=request.data)
        return Response({'message : User details retrieved succesfully'}, status=status.HTTP_200_OK)
