from rest_framework import serializers
from .models import CustomUsers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUsers
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        username = validated_data['username']
        email = validated_data['email']

        if CustomUsers.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "This username is already taken."})
        
        if CustomUsers.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "This email is already registered."})
       
       
        user = CustomUsers.objects.create_user(
            username=username,
            email=email,
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        
        return user