from rest_framework import serializers
from .models import *

class UserRegSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UserProfile
        fields = ['email', 'username', 'phone', 'firstName', 'lastName', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2', None)

        if password != password2:
            raise serializers.ValidationError("Password and confirm password do not match")

        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        return UserProfile.objects.create_user(password=password, **validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255)
    class Meta:
        model = UserProfile
        fields = ['email', 'password']  
      
from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'username', 'phone', 'firstName', 'lastName', 'profile_photo',
                  'coding_languages', 'dev_framework', 'databases', 'cloud', 'other']
