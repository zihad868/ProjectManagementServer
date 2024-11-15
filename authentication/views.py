from django.shortcuts import render
from authentication.models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


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
