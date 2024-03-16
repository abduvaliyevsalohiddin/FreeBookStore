from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdmin
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'phone', 'birthday', 'about_me')

    def create(self, validated_data):
        user = UserAdmin.objects.create_user(**validated_data)
        return user

    # def update(self, instance, validated_data):
    #     # instance.username = validated_data.get('username', instance.username)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     # instance.email = validated_data.get('email', instance.email)
    #     instance.password = validated_data.get('password', instance.password)
    #     # instance.phone = validated_data.get('phone', instance.phone)
    #     # instance.birthday = validated_data.get('birthday')
    #     instance.about_me = validated_data.get('about_me', instance)
    #     instance.save()
    #     return instance
