from rest_framework_simplejwt import serializers as jwtserializers
from core import models

class TokenObtainPairSerializer(jwtserializers.TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: models.User):
        token = super().get_token(user)
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['birth_date'] = str(user.birth_date)
        token['email'] = user.email
        token['username'] = user.username
        token['height'] = user.height
        token['weight'] = user.weight
        token['profile'] = user.profile.url if user.profile else ''
        token['slug'] = user.slug
        return token