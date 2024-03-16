from rest_framework import serializers
from core import models

class LocationSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    quest = serializers.CharField(required=True)
    slug = serializers.SlugField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = models.Location
        fields = [
            'latitude',
            'longitude',
            'quest',
            'slug',
            'created_at',
            'updated_at',
        ]
    
    def validate_quest(self, value):
        try:
            quest = models.Quest.objects.get(slug=value)
        except models.Quest.DoesNotExist:
            raise serializers.ValidationError({'quest': 'This quest slug doesn\'t exist.'})
        return quest

    def create(self, validated_data):
        quest = self.validate_quest(validated_data.pop('quest'))
        location = models.Location.objects.create(quest=quest, user=self.context['request'].user, **validated_data)
        return location
