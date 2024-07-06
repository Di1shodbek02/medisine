from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User


class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'middle_name', 'phone_number', 'birth_date')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            middle_name=validated_data['middle_name'],
            phone_number=validated_data['phone_number'],
            birth_date=validated_data['birth_date'],
        )
        return user


class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'middle_name', 'phone_number', 'birth_date')


class UpdateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'middle_name', 'phone_number', 'birth_date')


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'middle_name', 'phone_number', 'birth_date']
