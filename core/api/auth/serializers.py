from rest_framework import serializers
from core import models

class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = models.User
        fields = [
            'email',
            'username',
            'password1',
            'password2',
        ]

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({'password2': 'The two password fields didn\'t match.'})
        return data

    def create(self, validated_data):
        user = models.User()
        user.email = validated_data.pop('email')
        user.username = validated_data.pop('username')
        user.set_password(validated_data.pop('password1'))
        user.save()
        return user