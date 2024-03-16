from rest_framework import serializers
from core import models

class QuestSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    distance = serializers.IntegerField(read_only=True)
    prize = serializers.IntegerField(read_only=True)
    slug = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = models.Quest
        fields = [
            'name',
            'description',
            'distance',
            'prize',
            'slug',
            'created_at',
            'updated_at',
        ]
