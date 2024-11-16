from typing import Any, Dict
from django.shortcuts import render
from rest_framework_simplejwt.tokens import Token
from authentication.models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import generics, status, serializers
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# JWT
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

#Register
class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
    
      if serializer.is_valid():
         user = serializer.save()
         return Response({
            'user': CustomUserSerializer(user, context=self.get_serializer_context()).data,
            'message': "User Created Successfully"
        }, status=status.HTTP_201_CREATED)
      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Send Authentication Token & Refresh Token
class CustomTokenObtainedPairSerializer(TokenObtainPairSerializer):
  def validate(self, attrs):
     email = attrs.get('email')
     password = attrs.get('password')
     
     # Authenticate User 
     user = authenticate(email=email, password=password)
     
     
     if user is None:
       raise serializers.ValidationError({"detail": "Invalid email or password"})
     
     data = super().validate(attrs)
     data['email'] = user.email
     data['name'] = f"{user.first_name} {user.last_name}"
     data['id'] = user.id
     return data


class LoginView(TokenObtainPairView):
  serializer_class = CustomTokenObtainedPairSerializer
  

# Get User By Id
class GetUserByIdView(APIView):
    def get(self, request, user_id, *args, **kwargs):
        user = get_object_or_404(CustomUser, id=user_id)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
      
class UpdateUserView(APIView):
  def put(self, request, user_id, *args, **kwargs):
    user = get_object_or_404(CustomUser, id=user_id)
    serializer = CustomUserSerializer(user, data=request.data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def patch(self, request, user_id, *args, **kwargs):
        user = get_object_or_404(CustomUser, id=user_id)
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)