from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'is_staff',)
        model = User

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username', 'password',)
        model = User
        extra_kwargs = {"password":{'write_only': True}}

    def create(self,validated_data):
            user = User.objects.create(
                username=validated_data['username'],
                password = make_password(validated_data['password'])  
            )
            return user
