from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


# REgister Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], 
                        password = validated_data['password'],
                        first_name=validated_data['first_name'],
                        last_name=validated_data['last_name'])
        return user

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

# Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('id', 'username', 'email', 'first_name', 'last_name',)
        fields = ('__all__')
        # permissions = ()

# class TeacherSerializer():
#     class Meta:
#         permissions = ('can_add_user', 'can_view_user')
#         model = User
#         fields = ('id', 'first_name', 'last_name')

class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
        # fields = ('id', 'username', 'email', 'first_name', 'last_name',)

