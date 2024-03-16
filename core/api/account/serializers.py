from rest_framework import serializers
from django.contrib.auth import password_validation
from core import models

class AccountSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(required=True)
    height = serializers.FloatField(required=True)
    weight = serializers.FloatField(required=True)
    profile = serializers.ImageField(required=False)
    email = serializers.ReadOnlyField()
    slug = serializers.ReadOnlyField()

    class Meta:
        model = models.User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'birth_date',
            'height',
            'weight',
            'profile',
            'slug',
        ]

class PasswordChangeSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password1 = serializers.CharField(write_only=True, required=True)
    new_password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = models.User
        fields = [
            'old_password',
            'new_password1',
            'new_password2',
        ]

    def validate_old_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'old_password': 'Your old password was entered incorrectly'})
        return value
    
    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': 'The two password fields didn\'t match.'})
        password_validation.validate_password(data['new_password1'], self.context['request'].user)
        return data
    
    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password1'])
        user.save()
        return user